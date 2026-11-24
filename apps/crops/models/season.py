from django.db import models
from apps.common.models import TimeStampedModel


class CropSeason(TimeStampedModel):
    crop = models.ForeignKey(
        'crops.Crop',
        on_delete=models.CASCADE,
        related_name='seasons',
    )
    name = models.CharField(max_length=255, unique=True)
    name_bn = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name