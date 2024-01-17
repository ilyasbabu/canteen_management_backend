from django.db import models
from django.conf import settings

from common.models import TimeStamp

class Department(models.TextChoices):
    COMPUTER_SCIENCE = "COMPUTER_SCIENCE", "Computer Science"
    COMMERCE = "COMMERCE", "Commerce"
    HOTEL_MANAGEMENT = "HOTEL_MANAGEMENT", "Hotel Management"
    ENGLISH = "ENGLISH", "English"
    ECONOMICS = "ECONOMICS", "Economics"



class Student(TimeStamp):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.TextField(choices=Department.choices)

    def __str__(self):
        return self.user.username
