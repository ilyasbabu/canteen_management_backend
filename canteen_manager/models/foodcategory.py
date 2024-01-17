from django.db import models

from common.models import TimeStamp


class FoodCategory(TimeStamp):
    name = models.TextField()

    def __str__(self):
        return self.name
