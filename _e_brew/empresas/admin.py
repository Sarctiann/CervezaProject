from django.contrib import admin
from .models import Empresa, Producto, Precio


admin.site.register(Empresa)
admin.site.register(Producto)
admin.site.register(Precio)
