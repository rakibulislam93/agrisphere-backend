from django.db import models
from apps.common.models import TimeStampedModel


class CropCycle(TimeStampedModel):
    farmer = models.ForeignKey(
        'farmers.FarmerProfile',
        on_delete=models.CASCADE,
        related_name='crop_cycles',
    )
    land = models.ForeignKey(
        'lands.Land',
        on_delete=models.CASCADE,
        related_name='crop_cycles',
    )
    crop = models.ForeignKey(
        'crops.Crop',
        on_delete=models.CASCADE,
        related_name='crop_cycles',
    )
    variety = models.ForeignKey(
        'crops.CropVariety',
        on_delete=models.CASCADE,
        related_name='crop_cycles',
    )

    season = models.ForeignKey(
        'crops.CropSeason',
        on_delete=models.CASCADE,
        related_name='crop_cycles',
    )
    planting_date = models.DateField()
    expected_harvest_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return f"{self.crop.name} - {self.variety.name} - {self.season.name}"


    