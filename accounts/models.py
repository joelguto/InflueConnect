from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    INFLUENCER = 'influencer'
    ORGANISATION = 'organisation'

    USER_TYPE_CHOICES = [
        (INFLUENCER, 'Influencer'),
        (ORGANISATION, 'Organisation'),
    ]

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default=INFLUENCER
    )

    def __str__(self):
        return f"{self.username} ({self.user_type})"

