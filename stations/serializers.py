from rest_framework.serializers import ModelSerializer
from .models import Station


class StationSerializer(ModelSerializer):
    class Meta:
        model = Station
        fields = [
            'pk',
            'name',
            'latitude',
            'longitude',
            'trunk',
            'user',
        ]
