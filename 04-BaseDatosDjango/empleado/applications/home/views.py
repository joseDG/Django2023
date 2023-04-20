from django.shortcuts import render
from django.views.generic import (CreateView)

from .models import Prueba

#Importando el formulario
from .forms import PruebaForm

# Create your views here.
class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'
