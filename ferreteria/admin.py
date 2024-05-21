from django.contrib import admin
from .models import CategoriaProducto, Subcategoria, Producto

admin.site.register(CategoriaProducto)
admin.site.register(Subcategoria)
admin.site.register(Producto)