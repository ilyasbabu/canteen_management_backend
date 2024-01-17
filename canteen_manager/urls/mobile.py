from django.urls import path

from canteen_manager.views import mobile

urlpatterns = [
    path("list/", mobile.ListAPI.as_view()),
]