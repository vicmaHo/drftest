from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Con un decorador indico que es una ruta que funciona con metodos http
@api_view(['POST'])
def login(request):
    user =get_object_or_404 (User, username=request.data['username']) # si el usuario existe, se almacena si no, entonces devuelve un 404
    
    if not user.check_password(request.data['password']): # si la constraseña no es correcta
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST) # devuelvo un error y un estado 404
    
    token, created = Token.objects.get_or_create(user=user) # si el usuario existe, se crea el token
    
    serializer = UserSerializer(instance=user) # obtengo un dato serializado convertido en objeto json
    
    return Response({'token': token.key, 'created': created, 'user': serializer.data}, status=status.HTTP_200_OK)
    
        

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data) # creo instancia de serializer
    
    if serializer.is_valid(): # si el front me envia los datos correctos
        serializer.save()
        
        user = User.objects.get(username=serializer.data['username']) # obtengo el usuario
        user.set_password(serializer.data['password']) # guardo el usuario en la base de datos
        user.save()
        
        token = Token.objects.create(user=user) # creo el token
        
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED) # devuelvo el token, datos y un estado
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # en caso de no ser valido retorno un erro y un estado 400
    


@api_view(['POST'])
@authentication_classes([TokenAuthentication]) # significa que recibo una propiedad token que voy a validar
@permission_classes([IsAuthenticated]) # indico que esta es una ruta protegida por autenticación
def profile(request):
    print(request.user)
    return Response("You are authenticated!!", status=status.HTTP_200_OK)
