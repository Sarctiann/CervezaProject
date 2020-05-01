from django.urls import path, include
from rest_framework.routers import APIRootView, DefaultRouter
from .views import (

    UserViewSet,
    GroupViewSet,
    
    MarcaViewSet,
    ListaEstilosViewSet,
    EstiloViewSet,
    CervezaAsignadaViewSet,

    ClienteViewSet,

    ProvinciaViewSet,
    LocalidadViewSet,
    EmpresaViewSet,
    ProductorViewSet,

    MaquinaViewSet,
    CanillaViewSet,

    TarjetaViewSet,
    RegistroVentasViewSet
)


# https://stackoverflow.com/questions/17496249/in-django-restframework-how-to-change-the-api-root-documentation

class ApiAuthView(APIRootView):
    """Esta es la sección de Usuarios y Permisos"""
class ApiInicioView(APIRootView):
    """Esta es la raiz de la api de nuestro sistema de cervecería electronica"""

class AuthRouter(DefaultRouter):
    APIRootView = ApiAuthView

class RootRouter(DefaultRouter):
    APIRootView = ApiInicioView

router_auth = AuthRouter()

router = RootRouter()

# Módulo Autenticación
router_auth.register('usuario', UserViewSet, basename='usuario')
router_auth.register('grupo', GroupViewSet, basename='grupo')
# Módulo cervezas
router.register('marca', MarcaViewSet, basename='Marca')
router.register('lista-estilos', ListaEstilosViewSet, basename='ListaEstilos')
router.register('estilo', EstiloViewSet, basename='Estilos')
router.register('cerveza-asignada', CervezaAsignadaViewSet, basename='CervezaAsignada')
# Módulo clientes
router.register('cliente', ClienteViewSet, basename='Cliente')
# Módulo empresas
router.register('provincia', ProvinciaViewSet, basename='Provincia')
router.register('localidad', LocalidadViewSet, basename='Localidad')
router.register('empresa', EmpresaViewSet, basename='Empresa')
router.register('productor', ProductorViewSet, basename='Productor')
# Módulo maquinaria
router.register('maquina', MaquinaViewSet, basename='Maquina')
router.register('canilla', CanillaViewSet, basename='Canilla')
# Módulo Tarjetas
router.register('tarjetas', TarjetaViewSet, basename='Tarjeta')
router.register('registro', RegistroVentasViewSet, basename='RegistroVentas')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include(router_auth.urls)),
]
