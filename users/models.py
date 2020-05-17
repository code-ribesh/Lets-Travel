from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_NEPALI = "nep"
    LANGUAGE_CHOICES = (LANGUAGE_ENGLISH, "English"), (LANGUAGE_NEPALI, "Nepali")

    CURRENCY_USD = "usd"
    CURRENCY_NPR = "npr"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_NPR, "NPR"))

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    langauge = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=4, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)
