from rest_framework import serializers, viewsets
from base.models import HostedMeal

class HostedMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostedMeal 
