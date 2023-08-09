from django.db import models

# Create your models here.
class Persona(models.Model):
    """Model definition for Persona."""

    full_name = models.CharField('nombres', max_length=50)
    pais = models.CharField('Pais', max_length=30)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.IntegerField()
    apelativo = models.CharField('Apelativo', max_length=10)

    class Meta:
        """meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'persona'
        #no permiter repetir datos
        unique_together = ['pais', 'apelativo']
        #permite realizar validaciones
        contraints = [
            models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_name')
        ]
        #esto no permite crear el modelo en la base de datos
        abstract = True #no es necesarios crearlo en la base de datos

    def __str__(self):
        """unicode representation of Persona."""
        return self.full_name
    
#agregando herencia
class Empleados(Persona):
    empleado = models.CharField('Empleo', max_length=50)

class Cliente(Persona):
    email = models.EmailField('Email')