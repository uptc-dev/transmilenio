# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_expiring_authtoken.models import ExpiringToken
from rest_framework.authtoken.models import Token


class ObtainExpiringAuthToken(ObtainAuthToken):

    """View enabling username/password exchange for expiring token."""

    model = ExpiringToken

    def post(self, request):
        """Respond to POSTed username/password with token."""
        serializer = AuthTokenSerializer(data=request.data)

        if serializer.is_valid():
            token, _ = ExpiringToken.objects.get_or_create(
                user=serializer.validated_data['user']
            )

            token.delete()
            token = ExpiringToken.objects.create(
                user=serializer.validated_data['user']
            )
            return Response({
                'token': token.key,
                'username': token.user.username,
            })

        return Response(serializer.errors, status=400)


login = ObtainExpiringAuthToken.as_view()


@api_view(['DELETE'])
def logout(request):
    if request.method == 'DELETE':
        Token.objects.get(user=request.user).delete()
        return Response({})