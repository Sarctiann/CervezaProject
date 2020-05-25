from django.db import models


class Empresa(models.Model):
    id_localidad = models.ForeignKey('miscelaneos.Localidad', on_delete=models.CASCADE)
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
        return f"{self.business_name} de {self.id_localidad}"


class Producto(models.Model):
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    id_estilo = models.ForeignKey('productores.Estilo', on_delete=models.CASCADE)
    stock = models.FloatField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id_estilo} ({self.id_empresa})"


class Precio(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.FloatField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.quantity}ml ${self.price} | {self.id_producto}"    
