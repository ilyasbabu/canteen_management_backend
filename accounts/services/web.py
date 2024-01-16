import traceback
import sys
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from accounts.models import UserType


def web_login(request, template_name):
    error_msg = "Invalid Login Credentials"
    username, password, next_url = (
        request.POST.get("username"),
        request.POST.get("password"),
        request.POST.get("next_url"),
    )
    try:
        if username in [None, ""] or password in [None, ""]:
            raise Exception
        user = authenticate(username=username, password=password)
        if user is None:
            raise Exception
        if user.is_disabled:
            return render(
                request,
                template_name,
                {
                    "error": "Account has been deactivated.",
                    "next_url": next_url,
                    "username": username,
                    "password": password,
                },
            )
        if user.type != UserType.ADMIN:
            return render(
                request,
                template_name,
                {
                    "error": "Only Admin User can login via this portal.",
                    "next_url": next_url,
                    "username": username,
                    "password": password,
                },
            )
        login(request, user)
        return redirect(next_url)
    except Exception:
        error_info = "\n".join(traceback.format_exception(*sys.exc_info()))
        print(error_info)
        return render(
            request,
            template_name,
            {
                "error": error_msg,
                "next_url": next_url,
                "username": username,
                "password": password,
            },
        )
