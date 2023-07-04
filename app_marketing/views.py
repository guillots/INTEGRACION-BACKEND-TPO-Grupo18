from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView

from .models import Cliente

class ClientesBaseView(View):
    template_name = 'clientes.html'
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('clientes:all')


class ClientesListView(ClientesBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS VINOS
    """

class VinosDetailView(ClientesBaseView,DetailView):
    template_name = "cliente_detail.html"

class VinosCreateView(ClientesBaseView,CreateView):
    template_name = "cliente_create.html"
    extra_context = {
        "tipo": "Crear cliente"
    }


class VinosUpdateView(ClientesBaseView,UpdateView):
    template_name = "cliente_create.html"
    extra_context = {
        "tipo": "Actualizar cliente"
    }

class VinosDeleteView(ClientesBaseView,DeleteView):
    template_name = "cliente_delete.html"
    extra_context = {
        "tipo": "Borrar cliente"
    }


