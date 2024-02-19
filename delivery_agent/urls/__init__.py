from django.urls import include, path

app_name = "delivery_agent"

urlpatterns = [
    path("api/mobile/delivery/", include("delivery_agent.urls.mobile")),
    path("delivery/", include("delivery_agent.urls.web")),
]
