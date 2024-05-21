from django.urls import path, include
from .views import ApiRoot

urlpatterns = [
    path('', ApiRoot.as_view(), name='api-root'),
    path('cambio/', include('api.exchange.urls'))
]