from django.contrib import admin
from .models import Productor, Marca, Tipo, Estilo


admin.site.register(Productor)
admin.site.register(Marca)
admin.site.register(Tipo)
admin.site.register(Estilo)
