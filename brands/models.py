# brands/models.py
from django.db import models
from django.conf import settings
from organizations.models import Organization  # assuming org app is named 'organization'

class Brand(models.Model):
    brand = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255)

    # --Optional plain string for organization name, no FK
    brand_organization = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand_name} ({self.brand_organization})"