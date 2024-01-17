from django.urls import path

from accounts.views import web

urlpatterns = [
    path("", web.HomeView.as_view(), name="home"),
    path("login/", web.LoginView.as_view(), name="login"),
    path("logout/", web.LogoutView.as_view(), name="logout"),
]