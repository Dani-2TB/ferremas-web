from django.urls import path
from .views import CambioUsd

urlpatterns = [
    path('usd/', CambioUsd.as_view(), name='cambio-usd'),
]