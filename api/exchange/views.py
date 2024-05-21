from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from datetime import date
from bcchapi import Siete
from numpy import mean

"""
    Vista que retorna el valor del dolar en pesos chilenos para usarse en
    conversión. Utilizando el web service del banco central
"""
class CambioUsd(APIView):
    def get(self, request):
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
        
        try:
            valor = round(df_serie['value'].aggregate('mean'))
            return Response({"usd":valor}, status=status.HTTP_200_OK)
        except ValueError:
            return Response({'usd':'No data found'}, status.HTTP_404_NOT_FOUND)




