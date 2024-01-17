from django.urls import path

from canteen_manager.views import web

urlpatterns = [
    path(
        "canteen-manager/",
        web.CanteenManagerManageView.as_view(),
        name="canteen_manager",
    ),
]
