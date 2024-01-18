from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("accounts.urls", namespace="accounts")),
    path("", include("canteen_manager.urls", namespace="canteen_manager")),
    path("", include("teacher.urls", namespace="teacher")),
    path("", include("student.urls", namespace="student")),
]
