from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
#models
from .models import Empleado


# 3.Listar empleados por trabajo

# Create your views here.
# 1.Lista todos los empleados de la empresa (completo)
class ListaAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    model = Empleado

# 2.Listar todos los empleados que pertenecen a una area de la empresa
class ListByAreaEmpleado(ListView):
    """Lista empleados de una area"""
    template_name = 'empleados/list_by_Area.html'

    def get_queryset(self):
        #el codigo que yo quiero
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name = area
        )
        return lista

# 4.Listar los empleados por palabra clave
class ListEmpleadosByKword(ListView):
    """" lista empeladora por palabra clave """
    template_name = 'empleados/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('*********************')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista

# 5.Listar habilidades de un empleado
class ListaHabilidadesEmpleado(ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        return empleado.habilidades.all()

#Utilizacion de detailView - permite ver el detalle de cada empleado
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleados/detail_empleados.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context

class SuccessView(TemplateView):
    template_name = "empleados/success.html"

#permite crear un nuevo usuario
class EmpleadoCreateView(CreateView):
    template_name = "empleados/add.html"
    model = Empleado
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']  #('__all__')
    success_url = reverse_lazy('empleado_app:correcto') #se puede hacer la redireccion de la url

    def form_valid(self, form):
        #logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoUpdateView, self).form_valid(form)

#permite actualizar vista
class EmpleadoUpdateView(UpdateView):
    template_name = "empleados/update.html"
    model = Empleado
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades',]
    success_url = reverse_lazy('empleado_app:correcto')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print("Metodo Post")
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print("Metodo form valid")
        return super(EmpleadoUpdateView, self).form_valid(form)

#Permite eliminar empleado
class EmpleadoDeleteView(DetailView):
    model = Empleado
    template_name = "empleados/delete.html"
    success_url = reverse_lazy('empleado_app:correcto')