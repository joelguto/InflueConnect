# brands/serializers.py
from rest_framework import serializers
from .models import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'brand', 'brand_name', 'brand_organization']
        read_only_fields = ['brand_organization']
