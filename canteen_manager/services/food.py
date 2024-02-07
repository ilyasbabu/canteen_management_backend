from canteen_manager.models import Food, FoodCategory
from teacher.models import Teacher
from accounts.models import UserType
from django.core.exceptions import ValidationError
from django.db.models import F
from common.constants import NOT_CANTEEN_MANAGER_MSG, NOT_TEACHER_MSG, NOT_STUDENT_MSG
from common.services import upload_image


def get_food_list_for_manager(user):
    if user.type != UserType.MANAGER:
        raise ValidationError(NOT_CANTEEN_MANAGER_MSG)
    data = []
    foods = Food.objects.filter(is_active=True).order_by("-created_date")
    for food in foods:
        food_dct = {}
        food_dct["id"] = food.id
        food_dct["name"] = food.name
        food_dct["price"] = food.price
        food_dct["quantity"] = food.quantity
        food_dct["is_approved"] = food.is_approved
        food_dct["approved_by"] = food.approved_by.user.name if food.approved_by else ""
        food_dct["is_todays_special"] = food.is_todays_special
        data.append(food_dct)
    return data


def get_food_category(user):
    return FoodCategory.objects.filter(is_active=True).values("id", "name")


def create_food(user, name, quantity, price, category_id, image=None):
    if user.type != UserType.MANAGER:
        raise ValidationError(NOT_CANTEEN_MANAGER_MSG)
    try:
        category = FoodCategory.objects.get(id=category_id, is_active=True)
    except:
        raise ValidationError("Invalid Food Category")
    image_url = upload_image(image) if image else None
    food = Food(
        name=name,
        price=price,
        quantity=quantity,
        category=category,
        image_url=image_url,
        created_by=user,
        modified_by=user,
    )
    food.save()
    return food


def get_food_detail_for_manager(user, food_id):
    if user.type != UserType.MANAGER:
        raise ValidationError(NOT_CANTEEN_MANAGER_MSG)
    try:
        return (
            Food.objects.annotate(
                category_name=F("category__name"),
                approved_by_name=F("approved_by__user__name"),
            )
            .values(
                "id",
                "name",
                "price",
                "quantity",
                "is_approved",
                "is_todays_special",
                "category_name",
                "category_id",
                "image_url",
                "approved_by_id",
                "approved_by_name",
            )
            .get(id=food_id, is_active=True)
        )
    except:
        raise ValidationError("Invalid Food")


def update_food(user, food_id, name, quantity, price, category_id, image=None):
    if user.type != UserType.MANAGER:
        raise ValidationError(NOT_CANTEEN_MANAGER_MSG)
    try:
        food = Food.objects.get(id=food_id, is_active=True)
    except:
        raise ValidationError("Invalid Food")
    try:
        category = FoodCategory.objects.get(id=category_id, is_active=True)
    except:
        raise ValidationError("Invalid Food Category")
    food.name = name
    food.price = price
    food.quantity = quantity
    food.category = category
    food.modified_by = user
    if image:
        food.image_url = upload_image(image)
    food.save()


def delete_food(user, food_id):
    if user.type != UserType.MANAGER:
        raise ValidationError(NOT_CANTEEN_MANAGER_MSG)
    try:
        food = Food.objects.get(id=food_id, is_active=True)
    except:
        raise ValidationError("Invalid Food")
    food.is_active = False
    food.save()


def get_food_list_for_teacher(user):
    if user.type != UserType.TEACHER:
        raise ValidationError(NOT_TEACHER_MSG)
    data = []
    foods = Food.objects.filter(is_active=True).order_by("-created_date")
    for food in foods:
        food_dct = {}
        food_dct["id"] = food.id
        food_dct["name"] = food.name
        food_dct["price"] = food.price
        food_dct["quantity"] = food.quantity
        food_dct["image_url"] = food.image_url
        food_dct["is_approved"] = food.is_approved
        data.append(food_dct)
    return data


def get_food_detail_for_teacher(user, food_id):
    if user.type != UserType.TEACHER:
        raise ValidationError(NOT_TEACHER_MSG)
    try:
        return (
            Food.objects.annotate(
                category_name=F("category__name"),
            )
            .values(
                "id",
                "name",
                "price",
                "quantity",
                "is_approved",
                "category_name",
                "category_id",
                "image_url",
            )
            .get(id=food_id, is_active=True)
        )
    except:
        raise ValidationError("Invalid Food")


def approve_food(user, food_id):
    if user.type != UserType.TEACHER:
        raise ValidationError(NOT_TEACHER_MSG)
    try:
        food = Food.objects.get(id=food_id, is_active=True)
    except:
        raise ValidationError("Invalid Food")
    if food.is_approved:
        raise ValidationError("Food already approved")
    teacher = Teacher.objects.get(user=user)
    food.is_approved = True
    food.approved_by = teacher
    food.save()


def mark_as_todays_special(user, food_id):
    if user.type != UserType.MANAGER:
        raise ValidationError(NOT_CANTEEN_MANAGER_MSG)
    try:
        food = Food.objects.get(id=food_id, is_active=True)
    except:
        raise ValidationError("Invalid Food")
    if food.is_todays_special:
        raise ValidationError("Food already marked as todays special")
    if not food.is_approved:
        raise ValidationError("Food not Approved by supervising teacher")
    Food.objects.exclude(id=food_id).update(is_todays_special=False, modified_by=user)
    food.is_todays_special = True
    food.save()


def get_food_list_for_student(user):
    if user.type != UserType.STUDENT:
        raise ValidationError(NOT_STUDENT_MSG)
    data = []
    foods = Food.objects.filter(is_active=True, is_approved=True).order_by(
        "-created_date"
    )
    for food in foods:
        food_dct = {}
        food_dct["id"] = food.id
        food_dct["name"] = food.name
        food_dct["price"] = food.price
        food_dct["quantity"] = food.quantity
        food_dct["is_todays_special"] = food.is_todays_special
        food_dct["category"] = food.category.name
        food_dct["image_url"] = food.image_url
        data.append(food_dct)
    return data
