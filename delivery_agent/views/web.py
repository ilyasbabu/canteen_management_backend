from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from delivery_agent.services.delivery_agent import (
    get_agent_list,
    get_agent_detail,
    update_agent,
    create_agent,
    delete_agent,
)


class AgentListView(LoginRequiredMixin, View):
    template_name = "delivery_agent_list.html"

    def get(self, request):
        data = get_agent_list()
        return render(request, self.template_name, data)


class AgentCreateView(LoginRequiredMixin, View):
    template_name = "delivery_agent_create.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        create_agent(request)
        return redirect("delivery_agent:list")


class AgentDetailView(LoginRequiredMixin, View):
    template_name = "delivery_agent_detail.html"

    def get(self, request, id):
        try:
            data = get_agent_detail(id)
        except:
            return redirect("delivery_agent:list")
        return render(request, self.template_name, data)

    def post(self, request, id):
        update_agent(request, id)
        return redirect("delivery_agent:list")


class AgentDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        delete_agent(request, id)
        return redirect("delivery_agent:list")
