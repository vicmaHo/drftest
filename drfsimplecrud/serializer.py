# converitir los formatos de python a json
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: # especifico el modelo en el que esta basado el serializer
        model = User
        fields  = ['id', 'username', 'email', 'password']  #campos que se van a convertir desde un diccionario a un json