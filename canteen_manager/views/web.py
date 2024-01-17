from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

from canteen_manager.models import CanteenManager





class CanteenManagerManageView(LoginRequiredMixin,View):
    template_name = "canteen_manager.html"
    
    def get(self, request):
        canteen_manager = CanteenManager.objects.first()
        canteen_manager_user = canteen_manager.user
        data = {
            "username":canteen_manager_user.username,
            "name":canteen_manager_user.name,
            "mobile":canteen_manager_user.mobile
        }
        return render(request, self.template_name, data)
    
    def post(self, request):
        canteen_manager = CanteenManager.objects.first()
        canteen_manager_user = canteen_manager.user
        canteen_manager_user.username = request.POST.get("username")
        canteen_manager_user.name = request.POST.get("name")
        canteen_manager_user.mobile = request.POST.get("mobile")
        canteen_manager_user.save()
        return redirect("canteen_manager:canteen_manager")