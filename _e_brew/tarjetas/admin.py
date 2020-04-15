from django.contrib import admin
from .models import Tarjeta, RegistroVentas


# Register your models here.

class TarjetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'credit', 'active')
    list_filter = ('code', 'credit', 'active')

    list_editable = ("active", )

admin.site.register(Tarjeta, TarjetaAdmin)
admin.site.register(RegistroVentas)
