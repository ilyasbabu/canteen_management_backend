from django.urls import path

from teacher.views import mobile

urlpatterns = [
    path("food/list/", mobile.FoodListAPI.as_view()),
    path("food/detail/<int:id>/", mobile.FoodDetailAPI.as_view()),
    path("food/approve/<int:id>/", mobile.FoodApproveAPI.as_view()),
]