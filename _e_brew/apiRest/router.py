from django.urls import path, include
from rest_framework.routers import APIRootView, DefaultRouter
from .views import (

    UserViewSet,
    GroupViewSet,
    
    ClienteViewSet,
    TarjetaViewSet,

    PilonViewSet,
    CanillaViewSet,
    CanillaProductoViewSet,

    EmpresaViewSet,
    ProductoViewSet,
    PrecioViewSet,

    ProvinciaViewSet,
    LocalidadViewSet,
    RegistroVentaViewSet,
    CompraViewSet,

    ProductorViewSet,
    MarcaViewSet,
    TipoViewSet,
    EstiloViewSet,
)
from miscelaneos import urls

# https://stackoverflow.com/questions/17496249/in-django-restframework-how-to-change-the-api-root-documentation

class ApiInicioView(APIRootView):
    """Esta es la raiz de la api de nuestro sistema de cervecería electronica"""

class RootRouter(DefaultRouter):
    APIRootView = ApiInicioView


router = RootRouter()

# Módulo Autenticación
router.register('usuario', UserViewSet, basename='usuario')
router.register('grupo', GroupViewSet, basename='grupo')
# Módulo clientes
router.register('cliente', ClienteViewSet, basename='Cliente')
router.register('tarjeta', TarjetaViewSet, basename='Tarjeta')
# Módulo dispositivos
router.register('pilon', PilonViewSet, basename='Pilon')
router.register('canilla', CanillaViewSet, basename='Canilla')
router.register('canilla-producto', CanillaProductoViewSet, basename='CanillaProducto')
# Módulo empresas
router.register('empresa', EmpresaViewSet, basename='Empresa')
router.register('producto', ProductoViewSet, basename='Producto')
router.register('precio', PrecioViewSet, basename='Precio')
# Módulo miscelaneos
router.register('provincia', ProvinciaViewSet, basename='Provincia')
router.register('localidad', LocalidadViewSet, basename='Localidad')
router.register('registro', RegistroVentaViewSet, basename='RegistroVenta')
router.register('compra', CompraViewSet, basename='Compra')
# Módulo productores
router.register('productor', ProductorViewSet, basename='Productor')
router.register('marca', MarcaViewSet, basename='Marca')
router.register('tipo', TipoViewSet, basename='Tipo')
router.register('estilo', EstiloViewSet, basename='Estilos')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('action/', include(urls.urlpatterns))
]
