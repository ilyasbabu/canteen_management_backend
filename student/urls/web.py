from django.urls import path

from student.views import web

urlpatterns = [
    path("list/",web.StudentListView.as_view(),name="list"),
    path("delete/<int:id>",web.StudentDeleteView.as_view(),name="delete"),
]