from django.db import models
from django.conf import settings

from common.models import TimeStamp
from .foodcategory import FoodCategory
from teacher.models import Teacher


class Food(TimeStamp):
    name = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    is_todays_special = models.BooleanField(default=False)
    image_url = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
