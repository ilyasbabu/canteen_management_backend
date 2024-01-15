from django.urls import path

from accounts.api import mobile

urlpatterns = [
    path("login/", mobile.LoginAPI.as_view()),

]