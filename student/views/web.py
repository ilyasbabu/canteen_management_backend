from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from student.services.student import get_student_list, delete_student


class StudentListView(LoginRequiredMixin, View):
    template_name = "students_list.html"

    def get(self, request):
        data = get_student_list()
        return render(request, self.template_name, data)


class StudentDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        delete_student(request, id)
        return redirect("student:list")
