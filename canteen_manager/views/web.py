from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from canteen_manager.services.canteen_manager import (
    upddate_canteen_manager,
    get_canteen_manager_data,
    get_food_list,
)


class CanteenManagerManageView(LoginRequiredMixin, View):
    template_name = "canteen_manager.html"

    def get(self, request):
        data = get_canteen_manager_data()
        return render(request, self.template_name, data)

    def post(self, request):
        upddate_canteen_manager(request)
        return redirect("accounts:home")


class FoodListView(LoginRequiredMixin, View):
    template_name = "food_list.html"

    def get(self, request):
        data = get_food_list()
        return render(request, self.template_name, data)
