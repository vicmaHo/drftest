from rest_framework import serializers
from .models import Project

# Convertir un modelo en datos que van a ser consultados
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'technology', 'created_at') # campos de las tablas
        read_only_fields = ('created_at',) # este campo solo es para leer, no se puede actualizar ni eliminar
        
