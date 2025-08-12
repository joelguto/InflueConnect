# influencers/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import InfluencerCreateView, InfluencerViewSet

router = DefaultRouter()
router.register(r'influencers', InfluencerViewSet)
urlpatterns = [
    path('create/', InfluencerCreateView.as_view(), name='create-influencer'),
]

