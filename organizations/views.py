from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Organization
from .serializers import OrganizationSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only allow users to see their own organization profile
        return Organization.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically link the organization to the logged-in user
        serializer.save(user=self.request.user)
