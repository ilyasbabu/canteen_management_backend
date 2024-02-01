from accounts.models import UserType
from common.constants import NOT_STUDENT_MSG, NOT_CANTEEN_MANAGER_MSG
from django.core.exceptions import ValidationError
from django.db import transaction
from student.models import Order, OrderItem, Student, Status
from canteen_manager.models import Food
from datetime import datetime


def place_order(user, products, delivery_time):
    if user.type != UserType.STUDENT:
        raise ValidationError(NOT_STUDENT_MSG)

    student = Student.objects.get(user=user)
    today = datetime.now()
    year = datetime.strftime(today, "%Y")
    month = datetime.strftime(today, "%m")
    day = datetime.strftime(today, "%d")
    order_count = Order.objects.all().count()
    uid = "ORDER" + str(year) + str(month) + str(day) + str(order_count + 1).zfill(3)
    date_format = "%b %d %Y %H:%M:%S"

    with transaction.atomic():
        order = Order(
            order_id=uid,
            student=student,
            created_by=user,
            modified_by=user,
        )
        order.full_clean()
        order.save()

        total_price = 0
        total_quantity = 0

        for item in products:
            food = Food.objects.get(id=item["id"])
            quantity = item["quantity"]
            price = food.price * quantity
            if food.quantity < quantity:
                raise ValidationError("No enough Quantity for " + food.name)

            order_item = OrderItem(
                order=order,
                food=food,
                quantity=quantity,
                price=price,
                created_by=user,
                modified_by=user,
            )
            order_item.full_clean()
            order_item.save()

            food.quantity -= quantity
            food.full_clean()
            food.save()

            total_price += price
            total_quantity += quantity

        order.total_price = total_price
        order.total_quantity = total_quantity
        order.delivery_time = datetime.strptime(delivery_time, date_format)
        order.full_clean()
        order.save()


def get_order_list_for_student(user):
    if user.type != UserType.STUDENT:
        raise ValidationError(NOT_STUDENT_MSG)

    student = Student.objects.get(user=user)
    orders = Order.objects.filter(student=student, is_active=True)
    return orders


def get_order_detail_for_student(user, order_id):
    if user.type != UserType.STUDENT:
        raise ValidationError(NOT_STUDENT_MSG)
    order_not_found = "Order not found"
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        raise ValidationError(order_not_found)
    if order.student.user != user:
        raise ValidationError(order_not_found)
    return order


def get_order_status_dropdown_for_manager(user):
    if user.type != UserType.MANAGER:
        raise ValidationError(NOT_CANTEEN_MANAGER_MSG)
    return [{"value": value, "text": text} for value, text in Status.choices]


def change_order_status(user, order_id, status, remarks):
    if user.type != UserType.MANAGER:
        raise ValidationError(NOT_CANTEEN_MANAGER_MSG)
    order_not_found = "Order not found"
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        raise ValidationError(order_not_found)
    if status not in [choice.value for choice in Status]:
        raise ValidationError("Invalid Status")
    order.status = status
    order.remarks = remarks
    order.modified_by = user
    order.full_clean()
    order.save()


def get_order_list_for_manager(user):
    if user.type != UserType.MANAGER:
        raise ValidationError(NOT_CANTEEN_MANAGER_MSG)
    orders = Order.objects.filter(is_active=True)
    return orders


def get_order_detail_for_manager(user, order_id):
    if user.type != UserType.MANAGER:
        raise ValidationError(NOT_CANTEEN_MANAGER_MSG)
    order_not_found = "Order not found"
    try:
        order = Order.objects.get(id=order_id, is_active=True)
    except Order.DoesNotExist:
        raise ValidationError(order_not_found)
    return order
