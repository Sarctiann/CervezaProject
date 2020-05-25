"""
En Este archivo estan definidas las constantes y las validadciones
requeridas por views.py
"""


import os
from clientes.models import Tarjeta, Cliente
from dispositivos.models import CanillaProducto
from empresas.models import Precio


PROTOCOLO = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),'Protocolo.html'
)
ARDJSON = [  
    # IMPORTANTE: NO CAMBIAR EL ORDEN (tarj,canilla,cantidad)
    'card_code', 'beer_tap', 'quantity'
    # ------------------------------------------------------
]
INFO = '11: {}'
OK21 = '21: cantidad {}'
REJ41 = '41: Rechazado Tarjeta Invalida'
REJ42 = '42: Rechazado Cliente Invalido'
REJ43 = '43: Rechazado Saldo Insuficiente'
ERR51 = '51: Error, No se proveyó el contenido requerido'
ERR52 = '52: Error, Cerveza insuficiente'
ERR53 = '53: Error, Opción de Cantidad Invalida'
ERR54 = '54: Error, Canilla Asociada Invalida'
ERR55 = '54: Error, Canilla Fuera de Servicio'
ERR56 = '55: Pilon, Fuera de servicio'


def validar_REJ41(tarj):  # Optima
    """retorna True, si la Tarjeta es invalida"""
    if len(tarj) != 1:
        return True
    return False

def validar_REJ42(tarj):  # Optima
    """retorna True, si el Cliente es invalido"""
    if not tarj[0].id_cliente.user.is_active:
        return True
    return False

def validar_REJ43(tarj, precio):  # Optima
    """retorna True si el Saldo es insuficiente"""
    if tarj[0].credit < precio[0].price:
        return True
    return False

def validar_ERR51(data): # Optima 
    """retorna True, si no recibe el data requerido"""
    for i in ARDJSON:
        if i not in data:
            return True
    else:
        return False

def validar_ERR52(d_q, canProd): # Optima
    """retorna True, si la cerveza es insuficiente"""
    if float(d_q) > canProd[0].id_producto.stock:
        return True
    return False

def validar_ERR53(precio):  # Optima
    """retorna True, si 'quantity' es una opción invalida"""
    if len(precio) != 1:
        return True
    return False

def validar_ERR54(canProd):  # Optima
    """retorna True, si la CanillaProducto es Invalida"""
    if len(canProd) != 1 or not canProd[0].active:
        return True
    return False

def validar_ERR55(canProd):  # Optima
    """retorna True, si la Canilla está fuera de servicio"""
    if not canProd[0].id_canilla.active:
        return True
    return False

def validar_ERR56(canProd):  # Optima
    """retorna True, si el Pilon está fuera de servicio"""
    if not canProd[0].id_canilla.id_pilon.active:
        return True
    return False


def validar_peticion(request):  # Optima
    """si recibe un GET retorna información, si recibe un POST 
    realiza una serie de comprobaciones y retorna el returnado"""
    if request.method == 'GET':
        with open(PROTOCOLO, 'r') as protocolo:
            return INFO.format(protocolo.read())   
    if request.method == 'POST':
        data = request.data
        if validar_ERR51(request.data):
            return ERR51
        d_tarjeta = request.data[ARDJSON[0]]
        d_canilla = request.data[ARDJSON[1]]
        d_cantidad = request.data[ARDJSON[2]]
        tarj = Tarjeta.objects.filter(code=d_tarjeta)
        canProd = CanillaProducto.objects.filter(id=d_canilla)
        if validar_REJ41(tarj):
            return REJ41
        if validar_ERR54(canProd):
            return ERR54
        precio = Precio.objects.filter(
            id_producto=canProd[0].id_producto, quantity=d_cantidad)
        if validar_ERR53(precio):
            return ERR53
        if validar_REJ42(tarj):
            return REJ42
        if validar_ERR52(d_cantidad, canProd):
            return ERR52
        if validar_ERR55(canProd):
            return ERR55
        if validar_ERR56(canProd):
            return ERR56
        if validar_REJ43(tarj, precio):
            return REJ43

        return OK21.format(data[ARDJSON[2]])
