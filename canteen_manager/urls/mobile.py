from django.urls import path

from canteen_manager.views import mobile

urlpatterns = [
    path("food/list/", mobile.FoodListAPI.as_view()),
    path("food/category/dropdown/", mobile.FoodCategoryDropdownAPI.as_view()),
    path("food/create/", mobile.FoodCreateAPI.as_view()),
    path("food/detail/", mobile.FoodListAPI.as_view()),
    path("food/update/", mobile.FoodListAPI.as_view()),
    path("food/delete/", mobile.FoodListAPI.as_view()),
]
