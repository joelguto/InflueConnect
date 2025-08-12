# influencers/views.py
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Influencer
from .serializers import InfluencerSerializer, InfluencerOneSerializer


class InfluencerCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Ensure a user can only have one influencer profile
        if hasattr(request.user, 'influencer_profile'):
            return Response({"error": "Influencer profile already exists."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = InfluencerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InfluencerViewSet(viewsets.ModelViewSet):
    queryset = Influencer.objects.all()
    serializer_class = InfluencerOneSerializer