import uuid
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField

class Influencer(models.Model):
    influencer_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # Link to auth user (one-to-one)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='influencer_profile'
    )

    # Names
    first_name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=150, blank=True)  # middle name
    last_name = models.CharField(max_length=150)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{7,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    country = models.CharField(max_length=100, blank=True)
    social_tiktok = models.URLField(max_length=500, blank=True)
    social_instagram = models.URLField(max_length=500, blank=True)
    social_threads = models.URLField(max_length=500, blank=True)
    social_x = models.URLField(max_length=500, blank=True)          # Twitter/X
    social_linkedin = models.URLField(max_length=500, blank=True)
    interests = ArrayField(
        base_field=models.CharField(max_length=50),
        blank=True,
        default=list
    )

    description = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='influencers/profile_pictures/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Influencer"
        verbose_name_plural = "Influencers"

    def __str__(self):
        return f"{self.user.username} ({self.influencer_id})"
