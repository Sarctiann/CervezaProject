from django.db import models

from maquinaria.models import Canilla
from empresas.models import Productor

# Create your models here.
class Marca(models.Model):
    id_producer = models.ForeignKey(Productor, on_delete=models.CASCADE)
    description = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.producer

class ListaEstilos(models.Model):
    description = models.CharField(max_length=100)
    srm_range = models.CharField(max_length=6)

    def __str__(self):
        return self.description

class Estilo(models.Model):
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    id_listaEstilos = models.ForeignKey(ListaEstilos, on_delete=models.PROTECT)
    ibu = models.DecimalField(max_digits=4, decimal_places=2)
    srm = models.IntegerField()
    abv = models.DecimalField(max_digits=4, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        estilo = ListaEstilos.objects.get(pk=self.id_listaEstilos)
        marca = marca.objects.get(pk=self.id_marca)
        return f"{estilo} de {marca}"

class CervezaAsignada(models.Model):
    id_canilla = models.ForeignKey(Canilla, on_delete=models.SET_NULL, null=True)
    id_estilo = models.ForeignKey(Estilo, on_delete=models.CASCADE)
    liters = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        estilo = Estilos.objects.get(pk=self.id_estilo)
        canilla = Canilla.objects.get(pk=self.id_canilla)
        return f"{estilo} asignada a {canilla}"

    class Meta:
        verbose_name = "Cerveza Asignada"
        verbose_name_plural = "Cervezas Asignadas"

