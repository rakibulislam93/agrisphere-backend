from django.db import models


class Gender(models.TextChoices):
    MALE = "male", "Male"
    FEMALE = "female", "Female"
    OTHER = "other", "Other"


class Religion(models.TextChoices):
    ISLAM = "islam", "Islam"
    HINDUISM = "hinduism", "Hinduism"
    CHRISTIANITY = "christianity", "Christianity"
    BUDDHISM = "buddhism", "Buddhism"
    OTHER = "other", "Other"


class MaritalStatus(models.TextChoices):
    SINGLE = "single", "Single"
    MARRIED = "married", "Married"
    DIVORCED = "divorced", "Divorced"
    WIDOWED = "widowed", "Widowed"


class Division(models.TextChoices):
    DHAKA = "dhaka", "Dhaka"
    CHITTAGONG = "chittagong", "Chittagong"
    KHULNA = "khulna", "Khulna"
    RAJSHAHI = "rajshahi", "Rajshahi"
    BARISAL = "barisal", "Barisal"
    SYLHET = "sylhet", "Sylhet"
    RANGPUR = "rangpur", "Rangpur"
    MYMENSINGH = "mymensingh", "Mymensingh"