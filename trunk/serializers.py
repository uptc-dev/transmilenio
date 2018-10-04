# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.serializers import ModelSerializer
from .models import Trunk


class TrunkSerializer(ModelSerializer):
    class Meta:
        model = Trunk
        fields = [
            'first_letter',
            'name',
            'hex_color',
            'trunk_lenght',
            'pre_trunk_lenght',
        ]
