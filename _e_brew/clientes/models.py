from django.db import models
from django.contrib.auth.models import User
from empresas.models import Localidad
from clientes.avatar_storage import AvatarStorage, avatar_path


GENDER_CHOICES = [('Male', 'Masculino'), ('Female', 'Femenino')]

# Create your models here.
class Cliente(models.Model):
    user = models.OneToOneField(
        User, verbose_name='Usuario', on_delete=models.CASCADE)
    cellphone = models.IntegerField('Teléfono celular', null=True, blank=True)
    cuit = models.IntegerField('CUIT', null=True, blank=True)
    gender = models.CharField('Genero', choices=GENDER_CHOICES, max_length=15)
    id_localidad = models.ForeignKey(
        Localidad, verbose_name='Localidad', on_delete=models.CASCADE)
    avatar = models.ImageField('Foto de Perfil', 
        upload_to=avatar_path, storage=AvatarStorage(), null=True, blank=True)

    @property
    def username(self):
        return self.user.username
    @property
    def password(self):
        return self.user.password
    @property
    def email(self):
        return self.user.email
    @property
    def first_name(self):
        return self.user.first_name
    @property
    def last_name(self):
        return self.user.last_name
    @property
    def avatar_th(self):
        if self.avatar != '' and self.avatar != None:
            base_url = self.avatar.storage.base_url
            name, ext = self.avatar.name.rsplit('.', 1)
            avatar_th = base_url + name + '_th.' + ext
            return avatar_th

    def __str__(self):
        return self.user.username
