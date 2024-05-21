from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="ferreteria-index"),
  path("about/", views.about, name="ferreteria-about"),
  path("contacto/", views.contacto, name="ferreteria-contacto"),
  path("productos/", views.productos, name="ferreteria-productos"),
  path("productos/agregar/", views.agregar_producto, name="productos-agregar"),
  path("productos/editar/<int:pk>", views.editar_producto, name="productos-editar"),
  path("productos/eliminar/<int:pk>", views.eliminar_producto, name='productos-eliminar'),
  path("cambiarMoneda/<str:new>", views.cambiar_moneda, name='cambiar-moneda')
]