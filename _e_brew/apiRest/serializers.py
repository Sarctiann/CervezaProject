from rest_framework import serializers
from cervezas.models import Marca, ListaEstilos, Estilo, CervezaAsignada
from clientes.models import Cliente
from empresas.models import Provincia, Localidad, Empresa, Productor
from maquinaria.models import Maquina, Canilla
from tarjetas.models import Tarjeta, RegistroVentas


# Módulo cervezas

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
            model = Marca
            fields = '__all__'

class ListaEstilosSerializer(serializers.ModelSerializer):
    class Meta:
            model = ListaEstilos
            fields = '__all__'

class EstiloSerializer(serializers.ModelSerializer):
    class Meta:
            model = Estilo
            fields = '__all__'

class CervezaAsignadaSerializer(serializers.ModelSerializer):
    class Meta:
            model = CervezaAsignada
            fields = '__all__'


# Módulo clientes

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
            model = Cliente
            fields = '__all__'


# Módulo empresas

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
            model = Provincia
            fields = '__all__'

class LocalidadSerializer(serializers.ModelSerializer):
    class Meta:
            model = Localidad
            fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
            model = Empresa
            fields = '__all__'

class ProductorSerializer(serializers.ModelSerializer):
    class Meta:
            model = Productor
            fields = '__all__'


# Módulo maquinaria

class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
            model = Maquina
            fields = '__all__'

class CanillaSerializer(serializers.ModelSerializer):
    class Meta:
            model = Canilla
            fields = '__all__'


# Módulo Tarjetas

class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
            model = Tarjeta
            fields = '__all__'

class RegistroVentasSerializer(serializers.ModelSerializer):
    class Meta:
            model = RegistroVentas
            fields = '__all__'
