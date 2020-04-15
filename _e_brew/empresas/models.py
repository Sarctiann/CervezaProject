from django.db import models

# Create your models here.
class Provincia(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Localidad(models.Model):
    id_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Empresa(models.Model):
    id_localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    phone = models.IntegerField()
    cellphone = models.IntegerField()
    cuit = models.IntegerField()
    cuil = models.IntegerField()
    street = models.CharField(max_length=70)
    st_num = models.IntegerField()
    location = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        localidad = Localidad.objects.get(pk=self.id_localidad)
        return f"{self.business_name} de {localidad}"

class Productor(models.Model):
    id_localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    cellphone = models.IntegerField()
    date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
