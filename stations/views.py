from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist

from .models import Station
from .serializers import StationSerializer
from .forms import StationForm


@api_view(['POST', 'GET'])
def stations(request):
    if request.method == 'POST':
        form = StationForm(request.data)
        if form.is_valid():
            data = form.save()
            return Response({'pk': data.pk}, status=201)
        return Response(form.errors, status=400)
    if request.method == 'GET':
        return Response({'data': StationSerializer(Station.objects.all(), many=True).data}, status=200)


@api_view(['PUT', 'GET', 'DELETE'])
def station(request, pk):
    try:
        data = Station.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        form = StationForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return Response()
        return Response(form.errors, status=400)

    elif request.method == 'GET':
        return Response(StationSerializer(data).data)

    elif request.method == 'DELETE':
        data.delete()
        return Response()
