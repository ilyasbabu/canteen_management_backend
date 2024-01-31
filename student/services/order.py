from accounts.models import UserType
from common.constants import NOT_STUDENT_MSG
from django.core.exceptions import ValidationError
from django.db import transaction
from student.models import Order, OrderItem, Student
from canteen_manager.models import Food
from datetime import datetime


def place_order(user, products, delivery_time):
    if user.type != UserType.STUDENT:
        raise ValidationError(NOT_STUDENT_MSG)

    student = Student.objects.get(user=user)
    today = datetime.now()
    year = datetime.strftime(today, '%Y')
    month = datetime.strftime(today, '%m')
    day = datetime.strftime(today, '%d')
    order_count = Order.objects.all().count()
    uid = "ORDER" +str(year)+str(month)+str(day)+ str(order_count + 1).zfill(3)
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
                raise ValidationError("No enough Quantity for "+food.name)

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
