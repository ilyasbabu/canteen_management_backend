import os
import os.path
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_canteen.settings")

import django

django.setup()

from django.db import transaction
from django.contrib.auth import get_user_model

from accounts.models import UserType
from canteen_manager.models import CanteenManager, FoodCategory, Food
from teacher.models import Teacher
from student.models import Student, Department

User = get_user_model()


if __name__ == "__main__":
    print("Initializing Project....")
    with transaction.atomic():
        # ADMIN
        username = "admin"
        password = "1234"
        name = "admin"
        mobile = "1234567890"
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
        print(
            "admin credentials: \n username - " + username + "\n password - " + password
        )
        print("SuperAdmin User Created Sucessfully!!!\n")

        # CANTEEN MANAGER
        canteen_manager_username = "canteen_manager"
        canteen_manager_password = "1234"
        canteen_manager_name = "Canteen Manager"
        canteen_manager_mobile = "0987654321"
        canteen_manager_user = User(
            username=canteen_manager_username,
            name=canteen_manager_name,
            mobile=canteen_manager_mobile,
            type=UserType.MANAGER,
        )
        canteen_manager_user.set_password(canteen_manager_password)
        canteen_manager_user.full_clean()
        canteen_manager_user.save()
        CanteenManager.objects.create(
            user=canteen_manager_user, created_by=admin_user, modified_by=admin_user
        )
        print(
            "canteen manager credentials: \n username - "
            + canteen_manager_username
            + "\n password - "
            + canteen_manager_password
        )
        print("Canteen Manager Created Sucessfully!!!\n")

        # SUPERVISING TEACHERS
        teachers = [
            {
                "username": "teacher_1",
                "password": "1234",
                "mobile": "9999999999",
                "name": "Teacher 1",
            },
            {
                "username": "teacher_2",
                "password": "1234",
                "mobile": "8888888888",
                "name": "Teacher 2",
            },
        ]
        for teacher in teachers:
            teacher_user = User(
                username=teacher["username"],
                mobile=teacher["mobile"],
                name=teacher["name"],
                type=UserType.TEACHER,
            )
            teacher_user.set_password(teacher["password"])
            teacher_user.full_clean()
            teacher_user.save()
            Teacher.objects.create(
                user=teacher_user, created_by=admin_user, modified_by=admin_user
            )
            print(
                "Supervising Teacher credentials: \n username - "
                + teacher["username"]
                + "\n password - "
                + teacher["password"]
            )
            print(
                "Supervising Teacher- " + teacher["name"] + " Created Sucessfully!!!\n"
            )

        # FOOD
        food_categories = [
            "Vegetarian",
            "Non-Vegetarian",
            "Dessert",
            "Snacks",
            "Drinks",
        ]
        FoodCategory.objects.bulk_create(
            [
                FoodCategory(
                    name=category, created_by=admin_user, modified_by=admin_user
                )
                for category in food_categories
            ]
        )
        print(
            "Food Categories "
            + ", ".join(food_categories)
            + " Created Sucessfully!!!\n"
        )

        foods = [
            {
                "name": "Paneer Tikka",
                "quantity": 100,
                "price": "50",
                "category": "Vegetarian",
                "is_approved": True,
                "is_todays_special": True,
            },
            {
                "name": "Masala Dosa",
                "quantity": 100,
                "price": "50",
                "category": "Vegetarian",
                "is_approved": False,
                "is_todays_special": False,
            },
            {
                "name": "Chicken Tikka",
                "quantity": 100,
                "price": "50",
                "category": "Vegetarian",
                "is_approved": False,
                "is_todays_special": False,
            },
            {
                "name": "Chicken Biryani",
                "quantity": 100,
                "price": "50",
                "category": "Non-Vegetarian",
                "is_approved": True,
                "is_todays_special": False,
            },
            {
                "name": "Chicken 65",
                "quantity": 100,
                "price": "50",
                "category": "Non-Vegetarian",
                "is_approved": False,
                "is_todays_special": False,
            },
            {
                "name": "Chocolate Cake",
                "quantity": 100,
                "price": "50",
                "category": "Dessert",
                "is_approved": False,
                "is_todays_special": False,
            },
            {
                "name": "Chocolate Brownie",
                "quantity": 100,
                "price": "50",
                "category": "Dessert",
                "is_approved": False,
                "is_todays_special": False,
            },
            {
                "name": "Chicken Roll",
                "quantity": 100,
                "price": "50",
                "category": "Snacks",
                "is_approved": True,
                "is_todays_special": False,
            },
            {
                "name": "Chicken Sandwich",
                "quantity": 100,
                "price": "50",
                "category": "Snacks",
                "is_approved": True,
                "is_todays_special": False,
            },
            {
                "name": "Coke",
                "quantity": 100,
                "price": "50",
                "category": "Drinks",
                "is_approved": False,
                "is_todays_special": False,
            },
            {
                "name": "Pepsi",
                "quantity": 100,
                "price": "50",
                "category": "Drinks",
                "is_approved": False,
                "is_todays_special": False,
            },
            {
                "name": "Fanta",
                "quantity": 100,
                "price": "50",
                "category": "Drinks",
                "is_approved": False,
                "is_todays_special": False,
            },
            {
                "name": "Sprite",
                "quantity": 100,
                "price": "50",
                "category": "Drinks",
                "is_approved": False,
                "is_todays_special": False,
            },
            {
                "name": "Mango Shake",
                "quantity": 100,
                "price": "50",
                "category": "Drinks",
                "is_approved": False,
                "is_todays_special": False,
            },
            {
                "name": "Mango Juice",
                "quantity": 100,
                "price": "50",
                "category": "Drinks",
                "is_approved": True,
                "is_todays_special": False,
            },
            {
                "name": "Strawberry Shake",
                "quantity": 100,
                "price": "50",
                "category": "Drinks",
                "is_approved": False,
                "is_todays_special": False,
            },
            {
                "name": "Strawberry Juice",
                "quantity": 100,
                "price": "50",
                "category": "Drinks",
                "is_approved": False,
                "is_todays_special": False,
            },
            {
                "name": "Orange Shake",
                "quantity": 100,
                "price": "50",
                "category": "Drinks",
                "is_approved": False,
                "is_todays_special": False,
            },
        ]
        approved_by = Teacher.objects.first()
        Food.objects.bulk_create(
            [
                Food(
                    name=food["name"],
                    quantity=food["quantity"],
                    price=food["price"],
                    category=FoodCategory.objects.get(name=food["category"]),
                    created_by=admin_user,
                    modified_by=admin_user,
                    is_approved=food["is_approved"],
                    approved_by=approved_by if food["is_approved"] else None,
                    is_todays_special=food["is_todays_special"],
                )
                for food in foods
                if Food.objects.filter(name=food["name"]).exists() == False
            ]
        )
        print(
            "Food  "
            + ", ".join(food["name"] for food in foods)
            + " Created Sucessfully!!!\n"
        )

        # STUDENT
        students = [
            {
                "name": "Jhon",
                "password": "1234",
                "mobile": "9898989898",
                "department": Department.COMPUTER_SCIENCE,
            },
            {
                "name": "Jane",
                "password": "1234",
                "mobile": "8787878787",
                "department": Department.HOTEL_MANAGEMENT,
            },
        ]
        for student in students:
            student_user = User(
                username=student["mobile"],
                mobile=student["mobile"],
                name=student["name"],
                type=UserType.STUDENT,
            )
            student_user.set_password(student["password"])
            student_user.full_clean()
            student_user.save()
            Student.objects.create(
                user=student_user,
                department=student["department"],
                created_by=admin_user,
                modified_by=admin_user,
            )
            print(
                "Student credentials: \n username - "
                + student["mobile"]
                + "\n password - "
                + student["password"]
            )
            print("Student- " + student["name"] + " Created Sucessfully!!!\n")
