from django.shortcuts import render
from django.views.generic import TemplateView, ListView

#Importando el mdelo de bd
from .models import Prueba


# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/home.html'


class PruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset = ['A', 'B', 'C']
    context_object_name = 'lista_prueba'

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/prueba.html"
    context_object_name = "lista_prueba"
