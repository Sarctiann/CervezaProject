from django.db import models

# Create your models here.
class Cliente(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=70)
    
    # django ignora la longitud de los Integer aparentemente
    cellphone = models.IntegerField()
    cuit = models.IntegerField()
    
    # avatar = models.ImageField()
    avatar = models.CharField(max_length=255)
    original_avatar = models.CharField(max_length=255)
    gender = models.CharField(max_length=15)
    token = models.CharField(max_length=255)
    
    # Preguntar a Tin el funcionamiento
    date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
