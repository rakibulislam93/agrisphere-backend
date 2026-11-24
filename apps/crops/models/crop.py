from django.db import models
from apps.common.models import TimeStampedModel


class Crop(TimeStampedModel):
    name = models.CharField(max_length=255)
    name_bn = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="crops/images/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name