from django.contrib import admin


from .models import Provincia, Localidad, RegistroVenta, Compra

admin.site.register(Provincia)
admin.site.register(Localidad)
admin.site.register(RegistroVenta)
admin.site.register(Compra)
