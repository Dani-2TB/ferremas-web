# funciones de ayuda
def create_alert(type,message):
    return {"type": type, "message": message}


def create_moneda(request):
    try:
        moneda = request.session["moneda"]
    except KeyError:
        request.session["moneda"] = "clp"
        moneda = request.session["moneda"]
    
    return moneda

from datetime import date
from bcchapi import Siete

def obtener_valor_dolar():
    user = 'dan.ocaranza@duocuc.cl'
    password = 'Duoc2024'

    fecha_hoy = date.today()
    dias_atras = 1
    fecha_inicio = fecha_hoy.replace(day = fecha_hoy.day - dias_atras)
    id_serie = 'F073.TCO.PRE.Z.D'

    siete = Siete(user,password)

    df_serie = siete.cuadro(
        series = [id_serie],
        nombres = ['value'],
        desde = fecha_inicio.isoformat(),
        hasta = fecha_hoy.isoformat()
    )

    return round(df_serie['value'].aggregate('mean'))