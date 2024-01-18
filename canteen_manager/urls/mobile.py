from django.urls import path

from canteen_manager.views import mobile

urlpatterns = [
    path("food/list/", mobile.FoodListAPI.as_view()),
    path("food/category/dropdown/", mobile.FoodCategoryDropdownAPI.as_view()),
    path("food/create/", mobile.FoodCreateAPI.as_view()),
    path("food/detail/<int:id>/", mobile.FoodDetailAPI.as_view()),
    path("food/update/<int:id>/", mobile.FoodUpdateAPI.as_view()),
    path("food/delete/<int:id>/", mobile.FoodDeleteAPI.as_view()),
    path(
        "food/mark-as-todays-special/<int:id>/",
        mobile.FoodMarkTodaysSpecialAPI.as_view(),
    ),
]
