import os
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import AplicacionUsuario
from .serializer import AplicacionUsuarioAuthSerializer
from rest_framework.decorators import action

from django.http import JsonResponse
from rest_framework.decorators import api_view
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

            user_id = idinfo['sub']
            email = idinfo['email']
            name = idinfo['name']
            avatar = idinfo['picture']

            # Aquí puedes manejar la lógica de inicio de sesión, como crear un usuario o devolver un JWT
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
                # Obtiene el usuario en base al correo electrónico
                user = self.validate_user(user_data['data']['email'])
                
                # Verifica que la lista no esté vacía
                if user:
                    user[0]['avatar'] = user_data['data']['avatar']  # Añade 'avatar' al primer elemento
                    return Response(user, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
            else:
                # Retorna una respuesta de error con HTTP 400
                return Response({"error": user_data['message']}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
         # Token no válido
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
