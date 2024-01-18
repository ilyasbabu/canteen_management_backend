from django.urls import include, path

app_name = "student"

urlpatterns = [
    path("api/mobile/student/", include("student.urls.mobile")),
    path("student/", include("student.urls.web")),
]
