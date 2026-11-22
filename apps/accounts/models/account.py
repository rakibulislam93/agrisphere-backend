from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.common.models import TimeStampedModel
from apps.accounts.models.managers import CustomUserManager


class CustomUser(AbstractUser, TimeStampedModel):
    username = None
    first_name = None
    last_name = None

    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, unique=True)
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name