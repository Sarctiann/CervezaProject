from django.db import models


class Pilon(models.Model):
    code = models.CharField(max_length=10)
    date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Pilon {self.code}"

    class Meta:
        verbose_name_plural = 'Pilones'

class Canilla(models.Model):
    id_pilon = models.ForeignKey(Pilon, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Canilla {self.pk} -> {self.id_pilon}"

class CanillaProducto(models.Model):
    id_canilla = models.ForeignKey(Canilla, on_delete=models.CASCADE)
    id_producto = models.ForeignKey('empresas.producto', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pk} | {self.id_canilla} de {self.id_producto}"

    class Meta:
        verbose_name = 'Canilla -> Producto'
        verbose_name_plural = 'Canillas -> Productos'

    
