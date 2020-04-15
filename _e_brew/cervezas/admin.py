from django.contrib import admin

from .models import Marca, ListaEstilos, Estilo, CervezaAsignada

# Register your models here.
admin.site.register(Marca)
admin.site.register(ListaEstilos)
admin.site.register(Estilo)
admin.site.register(CervezaAsignada)
