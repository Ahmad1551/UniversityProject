from django.db import models
from django.contrib.auth.models import AbstractUser

from config.mixins import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    class UserTypeChoices(models.TextChoices):
        BUILDER = 'BUILDER', 'Builder'
        BUYER = 'BUYER', 'Buyer'
        DEALER = 'DEALER', 'Dealer'
        INVESTOR = 'INVESTOR', 'Investor'
        MANAGER = 'MANAGER', 'Manager'
        STAFF = 'STAFF', 'Staff'

    phone_number = models.CharField(max_length=13, null=True, blank=True)
    user_type = models.CharField(max_length=8, choices=UserTypeChoices.choices, default=UserTypeChoices.BUYER)
