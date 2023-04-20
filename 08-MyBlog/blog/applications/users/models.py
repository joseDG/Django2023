from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

#
from .managers import UserManager
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )

    email = models.EmailField(unique=True)
    full_name = models.CharField('Nombres', max_length=100)
    ocupation = models.CharField('Ocupacion', max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    date_birth = models.DateField('Fecha de nacimiento', blank=True, null=True)

    #verificar si los usuarios estan activos o inactivos
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    #requiere estos dos campos  para creaer un usuario | login
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['full_name']

    #creamos el objects UserManager traido del archivo | managers.py
    objects = UserManager()

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.full_name


