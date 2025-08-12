# influencers/serializers.py
from rest_framework import serializers
from .models import Influencer

class InfluencerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Influencer
        exclude = ['user', 'influencer_id', 'created_at', 'updated_at']

# your_app_name/serializers.py
class InfluencerOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Influencer
        fields = '__all__'
        read_only_fields = ['influencer_id', 'created_at', 'updated_at']
