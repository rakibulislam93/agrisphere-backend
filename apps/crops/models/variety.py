from django.db import models
from apps.common.models import TimeStampedModel


class CropVariety(TimeStampedModel):
    crop = models.ForeignKey(
        'crops.Crop',
        on_delete=models.CASCADE,
        related_name='varieties',
    )
    name = models.CharField(max_length=255)
    name_bn = models.CharField(max_length=255)

    created_by = models.ForeignKey(
        'farmers.FarmerProfile',
        on_delete=models.CASCADE,
        related_name='crop_varieties',
        null=True,
        blank=True,

    )
    
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name