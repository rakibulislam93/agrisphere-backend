from django.db import models
from apps.common.models import TimeStampedModel
from apps.lands.enums import LandType



class Land(TimeStampedModel):
    farmer = models.ForeignKey(
        "farmers.FarmerProfile",
        on_delete=models.CASCADE,
        related_name="lands",
    )
    name = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    land_type = models.CharField(
        max_length=20,
        choices=LandType.choices,
        default=LandType.OWNED,
    )
    location = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.farmer.user.full_name}"