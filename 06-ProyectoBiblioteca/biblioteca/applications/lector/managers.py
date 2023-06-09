import datetime

from django.db import models

from django.db.models import Q, Count, Avg, Sum
from django.db.models.functions import Lower


class PrestamoManager(models.Manager):
    """ procedimientos para prestamo """

    def libros_promedio_edades(self):
        resultado = self.filter(
            libro__id='15'
            #el aggregate devulve un diccionario sirve para funciones arimeticas
        ).aggregate(
            promedio_edad=Avg('lector__edad'),
            suma_edad=Sum('lector_edad'),
        )
        return resultado

    #agregando el annotate -> permite buscar en uno en uno
    def num_libros_prestados(self):
        resultado = self.values(
            'libro',
            'lector'
        ).annotate(
            num_prestados=Count('libro'),
            titulo=Lower('libro__titulo'),
        )
        for r in resultado:
            print('=========')
            print(r, r['num_prestados'])

        return resultado