from django.urls import path

from accounts.views import mobile

urlpatterns = [
    path("login/", mobile.LoginAPI.as_view()),
    path("change-password/", mobile.ChangePasswordAPI.as_view()),
]