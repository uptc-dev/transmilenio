from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist

from .models import Trunk
from .serializers import TrunkSerializer
from .forms import TrunkForm


@api_view(['POST', 'GET'])
# @permission_classes((permissions.AllowAny,))
def trunks(request):
    if request.method == 'POST':
        form = TrunkForm(request.data)
        if form.is_valid():
            data = form.save()
            return Response({'pk': data.pk}, status=201)
        return Response(form.errors, status=400)
    if request.method == 'GET':
        return Response({'data': TrunkSerializer(Trunk.objects.all(), many=True).data}, status=200)


@api_view(['PUT', 'GET', 'DELETE'])
def trunk(request, pk):
    try:
        data = Trunk.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        form = TrunkForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return Response()
        return Response(form.errors, status=400)

    elif request.method == 'GET':
        return Response(TrunkSerializer(data).data)

    elif request.method == 'DELETE':
        data.delete()
        return Response()
