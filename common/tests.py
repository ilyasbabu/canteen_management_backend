from django.test import TestCase
from django.db import transaction
from django.contrib.auth import get_user_model

from accounts.models import UserType
from canteen_manager.models import CanteenManager, FoodCategory, Food
from teacher.models import Teacher
from student.models import Student, Department

User = get_user_model()


class InitializeScriptTestCase(TestCase):
    def setUp(self):
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
            print("Student- " + student["name"] + " Created Sucessfully!!!\n")

    def test_users_created(self):
        admin_created = User.objects.filter(username="admin", type=UserType.ADMIN).exists()
        self.assertTrue(admin_created)

        canteen_manager_user = User.objects.filter(username="canteen_manager", type=UserType.MANAGER)
        self.assertTrue(canteen_manager_user.exists())

        canteen_manager_created = CanteenManager.objects.filter(user=canteen_manager_user[0]).exists()
        self.assertTrue(canteen_manager_created)

        teacher_user = User.objects.filter(username="teacher_1", type=UserType.TEACHER)
        self.assertTrue(teacher_user.exists())

        teacher_created = Teacher.objects.filter(user=teacher_user[0]).exists()
        self.assertTrue(teacher_created)

        student_user = User.objects.filter(username="9898989898", type=UserType.STUDENT)
        self.assertTrue(student_user.exists())

        student_created = Student.objects.filter(user=student_user[0]).exists()
        self.assertTrue(student_created)

        food_categories = FoodCategory.objects.filter(is_active=True)
        self.assertTrue(food_categories.exists())

        foods = Food.objects.filter(is_active=True)
        self.assertTrue(foods.exists())