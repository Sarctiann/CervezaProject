from rest_framework import viewsets
from .serializers import (

    Marca, MarcaSerializer,
    ListaEstilos, ListaEstilosSerializer,
    Estilo, EstiloSerializer,
    CervezaAsignada, CervezaAsignadaSerializer,

    Cliente, ClienteSerializer,

    Provincia, ProvinciaSerializer,
    Localidad, LocalidadSerializer,
    Empresa, EmpresaSerializer,
    Productor, ProductorSerializer,

    Maquina, MaquinaSerializer,
    Canilla, CanillaSerializer,

    Tarjeta, TarjetaSerializer,
    RegistroVentas, RegistroVentasSerializer
)

# Módulo cervezas

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ListaEstilosViewSet(viewsets.ModelViewSet):
    queryset = ListaEstilos.objects.all()
    serializer_class = ListaEstilosSerializer

class EstiloViewSet(viewsets.ModelViewSet):
    queryset = Estilo.objects.all()
    serializer_class = EstiloSerializer

class CervezaAsignadaViewSet(viewsets.ModelViewSet):
    queryset = CervezaAsignada.objects.all()
    serializer_class = CervezaAsignadaSerializer


# Módulo clientes

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


# Módulo empresas

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class LocalidadViewSet(viewsets.ModelViewSet):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer
    
class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class ProductorViewSet(viewsets.ModelViewSet):
    queryset = Productor.objects.all()
    serializer_class = ProductorSerializer


# Módulo maquinaria

class MaquinaViewSet(viewsets.ModelViewSet):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer

class CanillaViewSet(viewsets.ModelViewSet):
    queryset = Canilla.objects.all()
    serializer_class = CanillaSerializer


# Módulo Tarjetas

class TarjetaViewSet(viewsets.ModelViewSet):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer
    lookup_field = 'code'

class RegistroVentasViewSet(viewsets.ModelViewSet):
    queryset = RegistroVentas.objects.all()
    serializer_class = RegistroVentasSerializer
