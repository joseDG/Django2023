from django.db import models

# importarmos los managers
from .managers import AutorManager

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=20)
    edad = models.PositiveIntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id) + '-' + self.nombres + '-' + self.apellidos

#aplicamos herencia en los modelos
class Autor(Persona):

    objects = AutorManager()