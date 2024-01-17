from django.urls import path

from canteen_manager.views import mobile

urlpatterns = [
    path("food/list/", mobile.FoodListAPI.as_view()),
]