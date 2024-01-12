from django.conf import settings
from django.db import models


class TimeStamp(models.Model):
    """Model definition for TimeStamp.
    Abstract model that can be inhertied by all other models.
    Refers to fields present in all models.
    """

    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_created_by",
    )
    modified_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_modified_by",
    )

    class Meta:
        """Meta definition for TimeStamp."""

        abstract = True
        verbose_name = "TimeStamp"
        verbose_name_plural = "TimeStamps"