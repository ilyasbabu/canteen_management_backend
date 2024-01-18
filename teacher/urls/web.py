from django.urls import path

from teacher.views import web

urlpatterns = [
    path("list/",web.TeacherListView.as_view(),name="list"),
    path("create/",web.TeacherCreateView.as_view(),name="create"),
    path("detail/<int:id>/",web.TeacherDetailView.as_view(),name="detail"),
    path("delete/<int:id>/",web.TeacherDeleteView.as_view(),name="delete"),
]