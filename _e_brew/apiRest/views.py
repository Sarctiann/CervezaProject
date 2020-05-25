from rest_framework import viewsets
from .serializers import (

    User, UserSerializer,
    Group, GroupSerializer,

    Cliente, ClienteSerializer,
    Tarjeta, TarjetaSerializer,

    Pilon, PilonSerializer,
    Canilla, CanillaSerializer,
    CanillaProducto, CanillaProductoSerializer,

    Empresa, EmpresaSerializer,
    Producto, ProductoSerializer,
    Precio, PrecioSerializer,

    Provincia, ProvinciaSerializer,
    Localidad, LocalidadSerializer,
    RegistroVenta, RegistroVentaSerializer,
    Compra, CompraSerializer,

    Productor, ProductorSerializer,
    Marca, MarcaSerializer,
    Tipo, TipoSerializer,
    Estilo, EstiloSerializer,
)



# Módulo Autenticación

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['get']


# Módulo clientes

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.filter(user__is_active=True)
    serializer_class = ClienteSerializer
 
    def perform_destroy(self, instance):
        instance.user.is_active = False
        instance.save()


class TarjetaViewSet(viewsets.ModelViewSet):
    queryset = Tarjeta.objects.filter(active=True)
    serializer_class = TarjetaSerializer
    lookup_field = 'code'

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()


# Módulo dispositivos

class PilonViewSet(viewsets.ModelViewSet):
    queryset = Pilon.objects.filter(active=True)
    serializer_class = PilonSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()

class CanillaViewSet(viewsets.ModelViewSet):
    queryset = Canilla.objects.filter(active=True)
    serializer_class = CanillaSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()

class CanillaProductoViewSet(viewsets.ModelViewSet):
    queryset = CanillaProducto.objects.all()
    serializer_class = CanillaProductoSerializer


# Módulo empresas

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.filter(active=True)
    serializer_class = EmpresaSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.filter(active=True)
    serializer_class = ProductoSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()


class PrecioViewSet(viewsets.ModelViewSet):
    queryset = Precio.objects.all()
    serializer_class = PrecioSerializer


# Módulo Miscelaneos

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer


class LocalidadViewSet(viewsets.ModelViewSet):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer


class RegistroVentaViewSet(viewsets.ModelViewSet):
    queryset = RegistroVenta.objects.all()
    serializer_class = RegistroVentaSerializer
    http_method_names = ['get']


class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    http_method_names = ['get']


# Módulo productores


class ProductorViewSet(viewsets.ModelViewSet):
    queryset = Productor.objects.filter(active=True)
    serializer_class = ProductorSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.filter(active=True)
    serializer_class = MarcaSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()
        
        
class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer


class EstiloViewSet(viewsets.ModelViewSet):
    queryset = Estilo.objects.filter(active=True)
    serializer_class = EstiloSerializer

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()





