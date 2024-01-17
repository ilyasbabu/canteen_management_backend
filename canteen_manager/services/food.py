from canteen_manager.models import Food
from accounts.models import UserType
from django.core.exceptions import ValidationError


def get_food_list(user):
    if user.type != UserType.MANAGER:
        raise ValidationError("You Should be a CANTEEN MANAGER to access this API")
    data = []
    foods = Food.objects.filter(is_active=True)
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
