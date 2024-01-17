from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import UserType
from accounts.services.web import web_login


class HomeView(View):
    template_name = "home.html"

    def get(self, request):
        if request.user.is_anonymous:
            return redirect("accounts:login")
        else:
            if request.user.type == UserType.ADMIN:
                return render(request, self.template_name)
            else:
                logout(request)
                return redirect("accounts:login")


class LoginView(View):
    template_name = "login.html"
    next_url = "/"
    error_msg = ""

    def get(self, request):
        if request.user.is_anonymous:
            next_url = request.GET.get("next")
            if next_url in [None, "None", ""]:
                next_url = self.next_url
            return render(
                request,
                self.template_name,
                {
                    "error": self.error_msg,
                    "next_url": next_url,
                    "username": "",
                    "password": "",
                },
            )
        else:
            return redirect("accounts:home")

    def post(self, request):
        response = web_login(request, self.template_name)
        return response


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("accounts:login")
