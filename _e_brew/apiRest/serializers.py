from django.conf import settings
from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from clientes.models import Cliente, Tarjeta
from dispositivos.models import Pilon, Canilla, CanillaProducto
from empresas.models import  Empresa, Producto, Precio
from miscelaneos.models import Provincia, Localidad, RegistroVenta, Compra
from productores.models import Productor, Marca, Tipo, Estilo


# Módulo Autenticación

class UserSerializer(serializers.ModelSerializer):
    class Meta:
            model = User
            fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
            model = Group
            fields = '__all__'


# Módulo clientes

class ClienteSerializer(serializers.ModelSerializer):

    username = serializers.CharField(label='Nombre de usuario',
        style={'placeholder': 'requerido'}, required=True)
    password = serializers.CharField(label='Contraseña',
        style={'input_type': 'password', 'placeholder': 'requerido'}, required=True)
    email = serializers.CharField(
        label='Correo electrónico', required=False)

    first_name = serializers.CharField(
        label='Nombre/s', required=False)
    last_name = serializers.CharField(
        label='Apellido/s', required=False)
    avatar_th = serializers.SerializerMethodField(
        'get_avatar_th', label='Foto Miniatura')

    def get_avatar_th(self, obj):
        if obj.avatar_th:
            return self.context['request'].build_absolute_uri(obj.avatar_th)

    class Meta:
            model = Cliente
            fields = [
                'id','username','password','cellphone','email','cuit','gender',
                'first_name','last_name','id_localidad','date','avatar','avatar_th'
            ]

    def create(self, validated_data):
        if User.objects.filter(username=validated_data['username']).count():
            user = User.objects.get(username=validated_data['username'])
            user.set_password(validated_data['password'])
        else:
            user = User.objects.create_user(
                username= validated_data['username'],
                password= validated_data['password'],
            )
        user.email= validated_data.get('email', '')
        user.first_name = validated_data.get('first_name', '')
        user.last_name= validated_data.get('last_name', '')
        user.save()
        cliente = Cliente.objects.create(
            user= user,
            cellphone= validated_data.get('cellphone', ''),
            cuit= validated_data.get('cuit', ''),
            gender= validated_data.get('gender'),
            id_localidad = validated_data.get('id_localidad'),
            avatar = validated_data.get('avatar')
        )
        return cliente


    def update(self, instance, validated_data):
        user_instance = User.objects.get(username=instance.user.username)
        user_instance.username= validated_data.get('username', user_instance.username)
        if user_instance.password != validated_data['password']:
            user_instance.set_password(validated_data['password'])
        user_instance.email= validated_data.get('email', user_instance.email)
        user_instance.first_name= validated_data.get('first_name', user_instance.first_name)
        user_instance.last_name= validated_data.get('last_name', user_instance.last_name)
        user_instance.save()
        instance.user = user_instance
        instance.cellphone= validated_data.get('cellphone', instance.cellphone)
        instance.cuit= validated_data.get('cuit', instance.cuit)
        instance.gender= validated_data.get('gender', instance.gender)
        instance.id_localidad = validated_data['id_localidad'] or instance.id_localidad
        if validated_data['avatar'] is not None:
            instance.avatar= validated_data['avatar']
        instance.save()
        return instance

    def validate_username(self, value):
        if (self.context['request'].method == 'POST'
            and User.objects.filter(username=value).count() 
            and Cliente.objects.filter(user__username=value).count() ):
            raise serializers.ValidationError("Ese nombre de usuario no está disponible")
        return value

    if not settings.DEBUG:
        def validate_password(self, value):
            validate_password(value)
            return value


class TarjetaSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True, read_only=True)

    class Meta:
            model = Tarjeta
            fields = '__all__'


# Módulo dispositivos

class PilonSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True, read_only=True)

    class Meta:
            model = Pilon
            fields = '__all__'

class CanillaSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True, read_only=True)

    class Meta:
            model = Canilla
            fields = '__all__'

class CanillaProductoSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True, read_only=True)
    
    class Meta:
            model = CanillaProducto
            fields = '__all__'


# Módulo empresas

class EmpresaSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True, read_only=True)

    class Meta:
            model = Empresa
            fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True, read_only=True)

    class Meta:
            model = Producto
            fields = '__all__'


class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
            model = Precio
            fields = '__all__'


# Módulo Miscelaneos

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
            model = Provincia
            fields = '__all__'


class LocalidadSerializer(serializers.ModelSerializer):
    class Meta:
            model = Localidad
            fields = '__all__'
            depth=0


class RegistroVentaSerializer(serializers.ModelSerializer):
    class Meta:
            model = RegistroVenta
            fields = '__all__'


class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'


# Módulo productores

class ProductorSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True, read_only=True)

    class Meta:
            model = Productor
            fields = '__all__'


class MarcaSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True, read_only=True)

    class Meta:
            model = Marca
            fields = '__all__'


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
            model = Tipo
            fields = '__all__'


class EstiloSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True, read_only=True)

    class Meta:
            model = Estilo
            fields = '__all__'



