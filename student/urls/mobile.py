from django.urls import path

from student.views import mobile

urlpatterns = [
    path("food/list/", mobile.FoodListAPI.as_view()),
]