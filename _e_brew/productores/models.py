from django.db import models


class Productor(models.Model):
    id_localidad = models.ForeignKey('miscelaneos.Localidad', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    cellphone = models.IntegerField()
    date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"    

    class Meta:
        verbose_name_plural = 'Productores'


class Marca(models.Model):
    id_productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    description = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.description


class Tipo(models.Model):
    description = models.CharField(max_length=100)
    srm_range = models.CharField(max_length=6)

    def __str__(self):
        return self.description


class Estilo(models.Model):
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    id_tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    description = models.CharField(max_length=100)
    ibu = models.DecimalField(max_digits=4, decimal_places=2)
    srm = models.IntegerField()
    abv = models.DecimalField(max_digits=4, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.description
