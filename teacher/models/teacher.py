from django.db import models
from django.conf import settings

from common.models import TimeStamp


class Teacher(TimeStamp):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
