from student.models import Student, Department
from accounts.models import UserType
from accounts.services.mobile import create_user
from django.db import transaction
from django.core.exceptions import ValidationError


def get_department_dropdown():
    return [{"value": value, "text": text} for value, text in Department.choices]


def create_student(mobile, name, password, confirm_password, department):
    if password != confirm_password:
        raise ValidationError("Password and Confirm Password must be same")
    if Student.objects.filter(user__username=mobile).exists():
        raise ValidationError("Student already exists")
    if department not in [choice.value for choice in Department]:
        raise ValidationError("Invalid Department")
    if len(mobile) != 10:
        raise ValidationError("Mobile number must be 10 digits")
    try:
        int(mobile)
    except:
        raise ValidationError("Mobile number must be digits")
    with transaction.atomic():
        user = create_user(
            username=mobile,
            password=password,
            name=name,
            mobile=mobile,
            type=UserType.STUDENT,
        )
        student = Student(
            user=user, department=department, created_by=user, modified_by=user
        )
        student.full_clean()
        student.save()


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
