from django.urls import include, path

app_name = "canteen_manager"

urlpatterns = [
    path("api/mobile/canteen/", include("canteen_manager.urls.mobile")),
    path("", include("canteen_manager.urls.web")),
]