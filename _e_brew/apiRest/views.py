from rest_framework import viewsets
from .serializers import (

    User, UserSerializer,
    Group, GroupSerializer,

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

# Módulo Autenticación

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Módulo cervezas

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.filter(active=True)
    serializer_class = MarcaSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()

class ListaEstilosViewSet(viewsets.ModelViewSet):
    queryset = ListaEstilos.objects.all()
    serializer_class = ListaEstilosSerializer

class EstiloViewSet(viewsets.ModelViewSet):
    queryset = Estilo.objects.filter(active=True)
    serializer_class = EstiloSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()

class CervezaAsignadaViewSet(viewsets.ModelViewSet):
    queryset = CervezaAsignada.objects.all()
    serializer_class = CervezaAsignadaSerializer


# Módulo clientes

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.filter(user__is_active=True)
    serializer_class = ClienteSerializer
 
    def perform_destroy(self, instance):
        instance.user.is_active = False
        instance.save()


# Módulo empresas

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class LocalidadViewSet(viewsets.ModelViewSet):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer
    
class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.filter(active=True)
    serializer_class = EmpresaSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()

class ProductorViewSet(viewsets.ModelViewSet):
    queryset = Productor.objects.filter(active=True)
    serializer_class = ProductorSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()


# Módulo maquinaria

class MaquinaViewSet(viewsets.ModelViewSet):
    queryset = Maquina.objects.filter(active=True)
    serializer_class = MaquinaSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()

class CanillaViewSet(viewsets.ModelViewSet):
    queryset = Canilla.objects.filter(active=True)
    serializer_class = CanillaSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()


# Módulo Tarjetas

class TarjetaViewSet(viewsets.ModelViewSet):
    queryset = Tarjeta.objects.filter(active=True)
    serializer_class = TarjetaSerializer
    lookup_field = 'code'

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()

class RegistroVentasViewSet(viewsets.ModelViewSet):
    queryset = RegistroVentas.objects.all()
    serializer_class = RegistroVentasSerializer
