from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserType(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    MANAGER = "MANAGER", "Manager"
    TEACHER = "TEACHER", "Teacher"
    STUDENT = "STUDENT", "Student"



class User(AbstractUser):
    """Model definition for User."""

    first_name = None
    last_name = None
    email = None

    name = models.TextField()
    mobile = models.CharField(max_length=10)
    type = models.CharField(
        max_length=10, choices=UserType.choices, default=UserType.ADMIN
    )
    initial_password_reset = models.BooleanField(
        help_text="Initial Password Reset Status of the User", default=False
    )
    is_disabled = models.BooleanField(
        help_text="Disable Status of the User", default=False
    )
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_created_by",
        null=True,
        blank=True,
    )
    modified_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_modified_by",
        null=True,
        blank=True,
    )

    class Meta:
        """Meta definition for User."""

        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        """Unicode representation of User."""
        return self.username