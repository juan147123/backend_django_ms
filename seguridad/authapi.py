import os
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import AplicacionUsuario
from .serializer import AplicacionUsuarioAuthSerializer
from rest_framework.decorators import action
from django.http import JsonResponse
from google.oauth2 import id_token
from google.auth.transport import requests


class AplicacionUsuarioAuthViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = AplicacionUsuarioAuthSerializer

    def validate_user(self, username):

        usuario = AplicacionUsuario.objects.using('seguridadapp').filter(
            usuariorol__estado=1,
            id_aplicacion=os.getenv("ID_APLICACION"),
            username=username
        ).distinct()
        serializer = self.get_serializer(usuario, many=True)
        return serializer.data

    def validate_client_id(self, token):

        idinfo = id_token.verify_oauth2_token(
            token, requests.Request(), os.getenv("CLIENT_ID"))

        email = idinfo['email']
        avatar = idinfo['picture']

        return {
            "status": "success",
            "data": {
                "email": email,
                "avatar": avatar
            }
        }

    @action(detail=False, methods=['post'], url_path='validate')
    def validate(self, request):
        token = request.data.get('token')
        try:
            user_data = self.validate_client_id(token)

            if user_data and user_data['status'] == "success":

                user = self.validate_user(user_data['data']['email'])

                if user:
                    user[0]['avatar'] = user_data['data']['avatar']
                    return Response(user, status=status.HTTP_200_OK)
                else:
                    return Response({"status": 500, "message": "not found"}, status=500)
            else:

                return Response({"status": 500, "message": "not found"}, status=500)
        except ValueError as e:

            return Response({"status": 500, "message": str(e)}, status=500)
