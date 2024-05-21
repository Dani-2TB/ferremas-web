from django.urls import path, include
from .views import ProductosRoot

urlpatterns = [
    path('', ProductosRoot.as_view(), name='api-root'),
]