from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from teacher.services.teacher import (
    get_teacher_list,
    get_teacher_detail,
    update_teacher,
    create_teacher,
    delete_teacher,
)


class TeacherListView(LoginRequiredMixin, View):
    template_name = "teachers_list.html"

    def get(self, request):
        data = get_teacher_list()
        return render(request, self.template_name, data)


class TeacherCreateView(LoginRequiredMixin, View):
    template_name = "teachers_create.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        create_teacher(request)
        return redirect("teacher:list")


class TeacherDetailView(LoginRequiredMixin, View):
    template_name = "teachers_detail.html"

    def get(self, request, id):
        try:
            data = get_teacher_detail(id)
        except:
            return redirect("teacher:list")
        return render(request, self.template_name, data)

    def post(self, request, id):
        update_teacher(request, id)
        return redirect("teacher:list")


class TeacherDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        delete_teacher(request, id)
        return redirect("teacher:list")
