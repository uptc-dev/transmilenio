# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist

from .models import Zone
from .serializers import ZoneSerializer
from .forms import ZoneForm


@api_view(['POST', 'GET'])
def zones(request):
    if request.method == 'POST':
        form = ZoneForm(request.data)
        if form.is_valid():
            data = form.save()
            return Response({'pk': data.pk}, status=201)
        return Response(form.errors, status=400)
    if request.method == 'GET':
        return Response({'data': ZoneSerializer(Zone.objects.all(), many=True).data}, status=200)


@api_view(['PUT', 'GET', 'DELETE'])
def zone(request, pk):
    try:
        data = Zone.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        form = ZoneForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return Response()
        return Response(form.errors, status=400)

    elif request.method == 'GET':
        return Response(ZoneSerializer(data).data)

    elif request.method == 'DELETE':
        data.delete()
        return Response()
