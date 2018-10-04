from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from .models import Trunk
from .serializers import TrunkSerializer

@api_view(['POST', 'GET'])
@permission_classes((permissions.AllowAny,))
def trunks(request):
    if request.method == 'POST':
        return Response({}, status=201)
    if request.method == 'GET':
        return Response({'data': TrunkSerializer(Trunk.objects.all(), many=True).data}, status=200)
