from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer


# ViewSet-> Quien puede consultar mi modelo, Realización de operaciones basicas crud par ael modelo Project
class ProjectViewSet(viewsets.ModelViewSet):
    #indico la consulta
    queryset= Project.objects.all()
    permission_classes = [permissions.AllowAny] # indico las reglas de acceso, para todos los usuarios en este caso
    serializer_class = ProjectSerializer
    
    