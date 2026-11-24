from django.db import models


class LandType(models.TextChoices):
    OWNED = "owned", "Owned"
    LEASED = "leased", "Leased"
    BORGA = "borga", "Borga"