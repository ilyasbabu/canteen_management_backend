from student.models import Student


def get_student_list():
    student_list = []
    for student in Student.objects.filter(is_active=True):
        student_list.append(student)
    return {"student_list": student_list}


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.is_active = False
    student.save()
    student_user = student.user
    student_user.is_disabled = True
    student_user.save()
