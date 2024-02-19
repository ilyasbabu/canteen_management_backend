from django.urls import path

from delivery_agent.views import web

urlpatterns = [
    path("list/", web.AgentListView.as_view(), name="list"),
    path("create/", web.AgentCreateView.as_view(), name="create"),
    path("detail/<int:id>/", web.AgentDetailView.as_view(), name="detail"),
    path("delete/<int:id>/", web.AgentDeleteView.as_view(), name="delete"),
]
