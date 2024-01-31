from django.urls import path

from student.views import mobile

urlpatterns = [
    path("department/dropdown/", mobile.DepartmentDropdownAPI.as_view()),
    path("register/", mobile.StudentCreateAPI.as_view()),
    path("food/list/", mobile.FoodListAPI.as_view()),
    path("order/", mobile.FoodOrderAPI.as_view()),
    path("order/list/", mobile.OrderListAPI.as_view()),
    path("order/detail/<int:id>/", mobile.OrderDetailAPI.as_view()),
]