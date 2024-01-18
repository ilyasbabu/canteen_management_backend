from teacher.models import Teacher
from accounts.models import UserType, User


def get_teacher_list():
    teacher_list = []
    for teacher in Teacher.objects.filter(is_active=True):
        teacher_list.append(teacher)
    return {"teacher_list": teacher_list}


def get_teacher_detail(teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    return {
        "id": teacher_id,
        "username": teacher.user.username,
        "name": teacher.user.name,
        "mobile": teacher.user.mobile,
    }


def update_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id, is_active=True)
    teacher_user = teacher.user
    teacher_user.username = request.POST.get("username")
    teacher_user.name = request.POST.get("name")
    teacher_user.mobile = request.POST.get("mobile")
    teacher_user.save()


def create_teacher(request):
    teacher_user = User(
        username=request.POST.get("username"),
        name=request.POST.get("name"),
        mobile=request.POST.get("mobile"),
        type=UserType.TEACHER,
    )
    teacher_user.set_password("1234")
    teacher_user.full_clean()
    teacher_user.save()
    Teacher.objects.create(
        user=teacher_user, created_by=request.user, modified_by=request.user
    )


def delete_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    teacher.is_active = False
    teacher.modified_by = request.user
    teacher.save()
    teacher_user = teacher.user
    teacher_user.is_disabled = True
    teacher_user.save()
