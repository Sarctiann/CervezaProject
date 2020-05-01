from django.contrib.auth.models import User, Group
from rest_framework.views import Response
from rest_framework import serializers
from cervezas.models import Marca, ListaEstilos, Estilo, CervezaAsignada
from clientes.models import Cliente
from empresas.models import Provincia, Localidad, Empresa, Productor
from maquinaria.models import Maquina, Canilla
from tarjetas.models import Tarjeta, RegistroVentas


# Módulo Autenticación

class UserSerializer(serializers.ModelSerializer):
    class Meta:
            model = User
            fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
            model = Group
            fields = '__all__'


# Módulo cervezas

class MarcaSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True, read_only=True)

    class Meta:
            model = Marca
            fields = '__all__'

class ListaEstilosSerializer(serializers.ModelSerializer):
    class Meta:
            model = ListaEstilos
            fields = '__all__'

class EstiloSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True, read_only=True)

    class Meta:
            model = Estilo
            fields = '__all__'

class CervezaAsignadaSerializer(serializers.ModelSerializer):
    class Meta:
            model = CervezaAsignada
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
                'first_name','last_name','id_localidad','avatar','avatar_th'
            ]

    def create(self, validated_data):
        if User.objects.filter(username=validated_data['username']).count():
            user = User.objects.get(username=validated_data['username'])
        else:
            user = User.objects.create_user(
                username= validated_data['username'],
                password= validated_data['password'],
                email= validated_data.get('email', ''),
                first_name = validated_data.get('first_name', ''),
                last_name= validated_data.get('last_name', ''),
            )
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
        password = validated_data.get('password', user_instance.password)
        user_instance.set_password(password)
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


# Módulo empresas

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
            model = Provincia
            fields = '__all__'

class LocalidadSerializer(serializers.ModelSerializer):
    class Meta:
            model = Localidad
            fields = '__all__'
            depth=0

class EmpresaSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True, read_only=True)

    class Meta:
            model = Empresa
            fields = '__all__'

class ProductorSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True, read_only=True)

    class Meta:
            model = Productor
            fields = '__all__'


# Módulo maquinaria

class MaquinaSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True, read_only=True)

    class Meta:
            model = Maquina
            fields = '__all__'

class CanillaSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True, read_only=True)

    class Meta:
            model = Canilla
            fields = '__all__'


# Módulo Tarjetas

class TarjetaSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(initial=True, read_only=True)

    class Meta:
            model = Tarjeta
            fields = '__all__'

class RegistroVentasSerializer(serializers.ModelSerializer):
    class Meta:
            model = RegistroVentas
            fields = '__all__'
