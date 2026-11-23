from django.conf import settings
from django.db import models

from apps.common.models import TimeStampedModel
from apps.farmers.enums import (
    Gender,
    Religion,
    MaritalStatus,
    Division,
)


class FarmerProfile(TimeStampedModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="farmer_profile",
    )

    profile_image = models.ImageField(
        upload_to="farmers/profile_images/",
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        blank=True,
        null=True,
    )

    religion = models.CharField(
        max_length=20,
        choices=Religion.choices,
        blank=True,
        null=True,
    )

    marital_status = models.CharField(
        max_length=20,
        choices=MaritalStatus.choices,
        blank=True,
        null=True,
    )

    division = models.CharField(
        max_length=50,
        choices=Division.choices,
        blank=True,
        null=True,
    )

    district = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    upazila = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    union = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    village = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Farmer Profile - {self.user}"