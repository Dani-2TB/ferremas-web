from django.urls import path, include
from .views import ApiRoot

urlpatterns = [
    path('', ApiRoot.as_view(), name='api-root'),
    path('productos/', include('api.productos.urls')),
]