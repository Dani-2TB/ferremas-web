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