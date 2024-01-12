from django.db import models

from common.models import TimeStamp


class Image(TimeStamp):
    """Model definition for Image."""

    path = models.ImageField(upload_to="images/%Y-%m-%d")

    class Meta:
        """Meta definition for Image."""

        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        """Unicode representation of Image."""
        return self.path

    def save(self, *args, **kwargs):
        """Overriding the default save method."""
        self.full_clean()
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Image."""
        return ""
