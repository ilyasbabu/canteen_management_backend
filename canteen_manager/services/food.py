from canteen_manager.models import Food, FoodCategory
from accounts.models import UserType
from django.core.exceptions import ValidationError
from common.constants import NOT_CANTEEN_MANAGER_MSG


def get_food_list(user):
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


def create_food(user, name, quantity, price, category_id):
    if user.type != UserType.MANAGER:
        raise ValidationError(NOT_CANTEEN_MANAGER_MSG)
    try:
        category = FoodCategory.objects.get(id=category_id)
    except:
        raise ValidationError("Invalid Food Category")
    food = Food(
        name=name,
        price=price,
        quantity=quantity,
        category=category,
        created_by=user,
        modified_by=user,
    )
    food.save()
    return food
