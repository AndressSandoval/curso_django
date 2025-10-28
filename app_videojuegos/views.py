from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Sucursal, Empleado
from .forms import SucursalForm, EmpleadoFormSet
from django.db import transaction

# --- Vista de Lista ---
class SucursalListView(ListView):
    model = Sucursal
    template_name = 'listar_sucursales.html'
    context_object_name = 'sucursales' # Nombre de la variable en la plantilla

# --- Vista de Detalle ---
class SucursalDetailView(DetailView):
    model = Sucursal
    template_name = 'detalle_sucursal.html'
    context_object_name = 'sucursal'

# --- Vista de Creación (con FormSet) ---
class SucursalCreateView(CreateView):
    model = Sucursal
    form_class = SucursalForm
    template_name = 'formulario_sucursal.html'

    def get_context_data(self, **kwargs):
        # Añade el formset al contexto
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = EmpleadoFormSet(self.request.POST)
        else:
            data['formset'] = EmpleadoFormSet()
        data['titulo'] = 'Nueva Sucursal'
        return data

    def form_valid(self, form):
        # Guarda el formulario principal y el formset
        context = self.get_context_data()
        formset = context['formset']
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('app_videojuegos:detalle_sucursal', kwargs={'pk': self.object.pk})

# --- Vista de Actualización (con FormSet) ---
class SucursalUpdateView(UpdateView):
    model = Sucursal
    form_class = SucursalForm
    template_name = 'formulario_sucursal.html'

    def get_context_data(self, **kwargs):
        # Añade el formset al contexto
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = EmpleadoFormSet(self.request.POST, instance=self.object)
        else:
            data['formset'] = EmpleadoFormSet(instance=self.object)
        data['titulo'] = 'Editar Sucursal'
        return data

    def form_valid(self, form):
        # Guarda el formulario principal y el formset
        context = self.get_context_data()
        formset = context['formset']
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('app_videojuegos:detalle_sucursal', kwargs={'pk': self.object.pk})

# --- Vista de Borrado ---
class SucursalDeleteView(DeleteView):
    model = Sucursal
    template_name = 'confirmar_borrar.html'
    context_object_name = 'sucursal'
    success_url = reverse_lazy('app_videojuegos:listar_sucursales')