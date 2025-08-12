# organization/models.py
import uuid
from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator


class Organization(models.Model):
    organization_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='organization_profile'
    )

    name = models.CharField(max_length=255)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{7,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    country = models.CharField(max_length=100, blank=True)

    social_tiktok = models.URLField(max_length=500, blank=True)
    social_instagram = models.URLField(max_length=500, blank=True)
    social_threads = models.URLField(max_length=500, blank=True)
    social_x = models.URLField(max_length=500, blank=True)
    social_linkedin = models.URLField(max_length=500, blank=True)

    sector = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(
        upload_to='organizations/profile_pictures/',
        blank=True,
        null=True
    )

    brands = ArrayField(
        base_field=models.CharField(max_length=100),
        blank=True,
        default=list
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

    def __str__(self):
        return f"{self.name} ({self.user.email})"
