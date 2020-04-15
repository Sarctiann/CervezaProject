from django.db import models

# Create your models here.
class Maquina(models.Model):
    code = models.CharField(max_length=10)
    date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Maquina {self.code}"

class Canilla(models.Model):
    id_maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        maquina = Maquina.objects.get(pk=self.id_maquina)
        return f"Canilla {self.pk} de {maquina}"
