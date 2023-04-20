from django.db import models

#nos permite hacer la sentia tipo OR
from django.db.models import Q


class AutorManager(models.Manager):
    """ managers para el modelo autor """

    def buscar_autor(self, kword):
        resultado = self.filter(
            #permite buscar algo similar
            nombres__icontains=kword
        )

        resultado

    def buscar_autor2(self, kword):
        resultado = self.filter(
            Q(nombres__icontains=kword) | Q(apellidos__icontains=kword)
        )

        return resultado

    def buscar_autor3(self, kword):
        resultado = self.filter(
            nombres__icontains=kword
        ).exclude(
            Q(edad__icontains=35) | Q(edad__icontains=65)
        )

        return resultado

    def buscar_autor4(self, kword):
        resultado = self.filter(
            edad__gt=40,
            edad__lt=65
        ).order_by('apellidos', 'nombres', 'id')

        return resultado