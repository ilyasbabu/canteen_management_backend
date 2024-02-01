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
    path("order/list/", mobile.OrderListAPI.as_view()),
    path("order/detail/<int:id>/", mobile.OrderDetailAPI.as_view()),
    path("order/status/dropdown/", mobile.OrderStatusDropdownAPI.as_view()),
    path("order/status/change/<int:id>/", mobile.OrderStatusChangeAPI.as_view()),
]
