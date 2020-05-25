"""
Este archivo contiene las direcciones que no tienen tareas relacionadas
directamente con los modelos de los modulos.
"""


from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
    renderer_classes
)
from rest_framework.authentication import (
    TokenAuthentication, 
    SessionAuthentication
)
from .const_valids import validar_peticion


@api_view(['GET', 'POST'])
@renderer_classes([StaticHTMLRenderer])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def quiero_una(request):
    """esta vista es la encargada de servir una cerveza y realizar
    las operaciones pertinentes en la base de datos."""

    if (rta:=validar_peticion(request))[:2] == '21':
        """si es validado (codigo 21, seguún el protocolo) realiza 
        las operaciones en base de datos. En cualquier caso retorna
        retorna una representacion StaticHTML"""
        print('Te sirvo una cerveza')

        # Acá hay que implementar las modificaciones en base de datos...

    return Response(rta)