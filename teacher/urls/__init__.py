from django.urls import include, path

app_name = "teacher"

urlpatterns = [
    path("api/mobile/teacher/", include("teacher.urls.mobile")),
    path("teacher/", include("teacher.urls.web")),
]