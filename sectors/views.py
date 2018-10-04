from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist

from .models import Sector
from .serializers import SectorSerializer
from .forms import SectorForm


@api_view(['POST', 'GET'])
def sectors(request):
    if request.method == 'POST':
        form = SectorForm(request.data)
        if form.is_valid():
            data = form.save()
            return Response({'pk': data.pk}, status=201)
        return Response(form.errors, status=400)
    if request.method == 'GET':
        return Response({'data': SectorSerializer(Sector.objects.all(), many=True).data}, status=200)


@api_view(['PUT', 'GET', 'DELETE'])
def sector(request, pk):
    try:
        data = Sector.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        form = SectorForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return Response()
        return Response(form.errors, status=400)

    elif request.method == 'GET':
        return Response(SectorSerializer(data).data)

    elif request.method == 'DELETE':
        data.delete()
        return Response()
