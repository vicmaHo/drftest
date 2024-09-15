from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# ViewSet-> Quien puede consultar mi modelo, Realización de operaciones basicas crud par ael modelo Project
class ProjectViewSet(viewsets.ModelViewSet):
    #indico la consulta
    queryset= Project.objects.all()
    # permission_classes = [permissions.AllowAny] # indico las reglas de acceso, para todos los usuarios en este caso
    serializer_class = ProjectSerializer
    authentication_classes = [TokenAuthentication]  # Autenticación por token
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados
    
    