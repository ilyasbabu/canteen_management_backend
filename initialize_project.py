import os
import os.path
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_canteen.settings')

import django
django.setup()

from django.db import transaction
from django.contrib.auth import get_user_model

from accounts.models import UserType
from canteen_manager.models import CanteenManaer

User = get_user_model()


if __name__ == '__main__':
    print("Initializing Project....")
    with transaction.atomic():
        # ADMIN
        username = 'aadmin'
        password = '1234'
        name = 'admin'
        mobile = '1234567890'
        admin_user = User(
            username=username,
            name=name,
            mobile=mobile,
            is_superuser=True,
            is_staff=True,
            type=UserType.ADMIN,
        )
        admin_user.set_password(password)
        admin_user.full_clean()
        admin_user.save()
        print ("admin credentials: \n username - "+username+"\n password - "+password)
        print ("SuperAdmin User Created Sucessfully!!!\n")

        # CANTEEN MANAGER
        canteen_manager_username = 'canteen_manager'
        canteen_manager_password = '1234'
        canteen_manager_name = 'Canteen Manager'
        canteen_manager_mobile = '0987654321'
        canteen_manager_user = User(
            username=canteen_manager_username,
            name=canteen_manager_name,
            mobile=canteen_manager_mobile,
            type=UserType.MANAGER,
        )
        canteen_manager_user.set_password(canteen_manager_password)
        canteen_manager_user.full_clean()
        canteen_manager_user.save()
        CanteenManaer.objects.create(user=canteen_manager_user, created_by=admin_user, modified_by=admin_user)
        print ("canteen manager credentials: \n username - "+canteen_manager_username+"\n password - "+canteen_manager_password)
        print ("Canteen Manager User Created Sucessfully!!!\n")

        # SUPERVISING TEACHERS
        teachers = [
            {
                'username': 'teacher_1',
                'password': '1234',
                'mobile': '9999999999',
                'name': 'Teacher 1',
            },
            {
                'username': 'teacher_2',
                'password': '1234',
                'mobile': '8888888888',
                'name': 'Teacher 2',
            },
        ]