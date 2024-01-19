from django.urls import path

from student.views import mobile

urlpatterns = [
    path("department/dropdown/", mobile.DepartmentDropdownAPI.as_view()),
    path("register/", mobile.StudentCreateAPI.as_view()),
    path("food/list/", mobile.FoodListAPI.as_view()),
]