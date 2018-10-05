# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.serializers import ModelSerializer
from .models import Zone


class ZoneSerializer(ModelSerializer):
    class Meta:
        model = Zone
        fields = [
            'pk',
            'name',
            'sector',
            'trunk',
        ]
