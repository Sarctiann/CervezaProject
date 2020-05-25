from django.db import models


class Provincia(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Localidad(models.Model):
    id_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.description} de {self.id_provincia}"

    class Meta:
        verbose_name_plural = 'Localidades'


class RegistroVenta(models.Model):
    id_can_prod = models.ForeignKey(
        'dispositivos.CanillaProducto', on_delete=models.CASCADE)
    id_tarjeta = models.ForeignKey('clientes.Tarjeta', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    price = models.FloatField()
    quantity = models.FloatField()

    def __str__(self):
        registro = " | ".join([
            self.pk,
            self.date,
            self.price,
            self.quantity,
            self.tarjeta,
            self.id_can_prod,
        ])
        return registro

    class Meta:
        verbose_name = 'Registro de Ventas'
        verbose_name_plural = 'Registros de Ventas'


class Compra(models.Model):
    id_estilo = models.ForeignKey(
        'productores.Estilo', on_delete=models.CASCADE)
    id_empresa = models.ForeignKey(
        'empresas.Empresa', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    liters = models.FloatField()

    def __str__(self):
        registro = " | ".join([
            self.pk,
            self.date,
            self.liters,
            self.id_empresa,
            self.id_estilo,
            self.id_estilo.id_marca,
        ])
        return registro
    
