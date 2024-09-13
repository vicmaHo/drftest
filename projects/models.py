from django.db import models

# Create your models here.

# Modelo de proyecto, especificando campos que seran mapeados a la base de datos
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  