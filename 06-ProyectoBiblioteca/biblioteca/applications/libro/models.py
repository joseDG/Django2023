from django.db import models
from django.db.models.signals import post_save

#Importacion de autor
from applications.autor.models import Autor

#Importar managers
from .managers import LibroManager, CategoriaManager


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    #agregando el managers
    objects = CategoriaManager()

    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='categoria_libro' #permite buscar por ID
    )
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(upload_to='portada')
    visitas = models.PositiveIntegerField()
    stok = models.PositiveIntegerField(default=0)

    objects = LibroManager()

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return str(self.id) + '-' + self.titulo