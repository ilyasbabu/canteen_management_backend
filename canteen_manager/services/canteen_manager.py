from canteen_manager.models import CanteenManager, Food


def get_canteen_manager_data():
    canteen_manager = CanteenManager.objects.first()
    canteen_manager_user = canteen_manager.user
    return {
        "username": canteen_manager_user.username,
        "name": canteen_manager_user.name,
        "mobile": canteen_manager_user.mobile,
    }

def upddate_canteen_manager(request):
    canteen_manager = CanteenManager.objects.first()
    canteen_manager_user = canteen_manager.user
    canteen_manager_user.username = request.POST.get("username")
    canteen_manager_user.name = request.POST.get("name")
    canteen_manager_user.mobile = request.POST.get("mobile")
    canteen_manager_user.save()

def get_food_list():
    food_list = Food.objects.filter(is_active=True)
    return {
        "food_list": food_list
    }
