from django.conf import settings
from django.db import models

from common.models import TimeStamp


class UserAuthToken(TimeStamp):
    """Model definition for UserAuthToken."""

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key = models.TextField()
    is_expired = models.BooleanField(default=False)

    class Meta:
        """Meta definition for UserAuthToken."""

        verbose_name = "UserAuthToken"
        verbose_name_plural = "UserAuthTokens"

    def __str__(self):
        """Unicode representation of UserAuthToken."""
        return self.key

    def save(self, *args, **kwargs):
        """Overriding the default save method."""
        self.full_clean()
        return super().save(*args, **kwargs)
