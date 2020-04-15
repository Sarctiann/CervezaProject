from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    
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

router = DefaultRouter()
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
]
