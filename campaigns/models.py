# campaigns/models.py
from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from organizations.models import Organization
from brands.models import Brand


class Campaign(models.Model):
    campaign_name = models.CharField(max_length=255)

    # For now, keep these as strings for simplicity (can be FK later)
    campaign_brand = models.CharField(max_length=255)
    campaign_organization = models.CharField(max_length=255)

    campaign_start_date = models.DateField()
    campaign_end_date = models.DateField()

    # Creators array of UUIDs or usernames or whatever identifier you prefer
    creators = ArrayField(
        base_field=models.CharField(max_length=255),  # e.g., usernames or influencer IDs
        blank=True,
        default=list
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"

    def __str__(self):
        return f"{self.campaign_name} ({self.campaign_brand})"
