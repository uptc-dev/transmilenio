from rest_framework.serializers import ModelSerializer
from .models import Trunk


class TrunkSerializer(ModelSerializer):
    class Meta:
        model = Trunk
        fields = [
            'pk',
            'first_letter',
            'name',
            'hex_color',
            'trunk_lenght',
            'pre_trunk_lenght',
        ]
