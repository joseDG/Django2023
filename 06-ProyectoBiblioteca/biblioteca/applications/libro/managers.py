import datetime

from django.db import models

from django.db.models import Q,Count

#esta se importa realizando en la shell de postgres se llama trigram
from django.contrib.postgres.search import TrigramSimilarity


class LibroManager(models.Manager):
    """ managers para el modelo autor """

    def listar_libros(self, kword):
        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=('2000-01-01', '2010-01-01')
        )

        return resultado

    #busquedas con triagram
    def listar_libros_trg(self, kword):
        if kword:
            resultado = self.filter(
                titulo__trigram_similar=kword,
            )
            return resultado
        else:
            return self.all()[:10]

    def listar_libros2(self, kword, fecah1, fecha2):

        date1 = datetime.datetime.strptime(fecah1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=(date1, date2)
        )

        return resultado

    #consultas avanzada - 
    def listar_libros_categoria(self, categoria):
        return self.filter(
            categoria__id=categoria
        ).order_by('titulo')

    def add_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        return libro

    def libros_num_prestamos(self):
        resultado = self.annotate(
            num_prestamos=Count('libro_prestamo')
        )
        for r in resultado:
            print('============')
            print(r, r.num_prestamos)

        return resultado

#creando un manager para categoria
class CategoriaManager(models.Manager):
    """ managers para el modelo autor """

    def categoria_por_autor(self, autor):
        return self.filter(
            #hace referencia de categoria-libro-autor
            categoria_libro__autores__id=autor
        ).distinct() #trae las consultas que no se repitan

    def listar_categoria_libros(self):
        #nos devuleve la operacion arimetica
        #agregando annotate() -> el conteo de objetos
        resultado = self.annotate(
            num_libros=Count('categoria_libro')
        )
        for r in resultado:
            print('********')
            print(r, r.num_libros)
        return resultado
    
#probando la shell
#python manage.py shell
#creando consultas
#from applications.libro.models import *
#Categoria.objects.categoria_por_autor('1')
#