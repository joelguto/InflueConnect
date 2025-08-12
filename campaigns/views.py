# campaigns/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Campaign
from .serializers import CampaignSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # You can customize filtering to only show campaigns relevant to the user's organization/brands later
        return Campaign.objects.all()

    def perform_create(self, serializer):
        # You can add logic here later to validate or set campaign_organization or campaign_brand
        serializer.save()
