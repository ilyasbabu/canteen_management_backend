from django.urls import include, path

app_name = "accounts"

urlpatterns = [
    path("api/mobile/", include("accounts.urls.mobile")),
    path("", include("accounts.urls.web")),
]