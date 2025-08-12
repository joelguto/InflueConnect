# brands/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Brand
from .serializers import BrandSerializer

class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only brands belonging to the user's organization
        user_org = self.request.user.organization_profile
        return Brand.objects.filter(brand_organization=user_org)

    def perform_create(self, serializer):
        # Automatically set brand_organization based on current user's organization
        user_org = self.request.user.organization_profile
        serializer.save(brand_organization=user_org)
