from django.db import models

#nos permite utilizar operadores logicos como or and
from django.db.models import Q


class AutorManager(models.Manager):
    """ managers para el modelo autor """

    #permite listar los autores
    def listar_autores(self):
         return self.all()

    def buscar_autor(self, kword):
        #se aplica un filtro
        resultado = self.filter(
            #permite buscar algo similar
            nombres__icontains=kword
        )

        return resultado

    #consulta por nombres o apellidos
    def buscar_autor2(self, kword):
        resultado = self.filter(
            Q(nombres__icontains=kword) | Q(apellidos__icontains=kword)
        )

        return resultado

    #consultar por nombre y excluir a personas con edad 35 y 65
    def buscar_autor3(self, kword):
        resultado = self.filter(
            nombres__icontains=kword
        ).exclude(
            Q(edad__icontains=35) | Q(edad__icontains=65)
        )

        return resultado

    #lista autores cuya edad sean mayores 40 || 65 
    def buscar_autor4(self, kword):
        resultado = self.filter(
            edad__gt=40,
            edad__lt=65
        ).order_by('apellidos', 'nombres', 'id')

        return resultado
