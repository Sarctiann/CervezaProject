import uuid
from django.db import models

from clientes.models import Cliente
from empresas.models import Empresa
from maquinaria.models import Canilla

# Create your models here.
class Tarjeta(models.Model):
    code = models.CharField(max_length=6, blank=False, null=False, unique=True)
    credit = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Tarjeta {self.code}"


class RegistroVentas(models.Model):
    id_tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    id_canilla = models.ForeignKey(Canilla, on_delete=models.PROTECT)
    credit = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        tarjeta = Tarjeta.objects.get(pk=self.id_tarjeta)
        return f"Pertenece a {tarjeta}"

    class Meta:
        verbose_name = "Registro de Venta"
        verbose_name_plural = "Registro de Ventas"

