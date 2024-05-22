from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CategoriaProducto, Producto
from .forms import ProductFrom
from django.contrib.auth.decorators import login_required

from .helpers import create_alert, create_moneda

# Vistas principales
def index(request):
  moneda = create_moneda(request)
  context = {"moneda": moneda}
  return render(request,'ferreteria/index.html', context)

def about(request):
  context = {}
  return render(request,'ferreteria/about.html', context)

def contacto(request):
  context = {}
  return render(request,'ferreteria/contact.html', context)

from .helpers import obtener_valor_dolar

# Vistas Productos
def productos(request):
  moneda = create_moneda(request)
  context = {"moneda": moneda}
  try:
    context.update({"alert":request.session["alert"]})
    del request.session["alert"]
  except KeyError:
    pass

  valor_conversion = 1

  qs_categorias = CategoriaProducto.objects.all()
  qs_productos = Producto.objects.all()

  if moneda == 'usd':
    valor = obtener_valor_dolar()
    if valor > 0:
      valor_conversion = valor

  catalogo = {}
  for c in qs_categorias:
    lista_productos = list(qs_productos.filter(categoria = c))
    if valor_conversion > 1:
      for p in lista_productos:
        p.precio = round((p.precio/ valor_conversion)/0.25) * 0.25
    if lista_productos: catalogo[c.nombre] = lista_productos
  
  context.update({"catalogo":catalogo}) 

  return render(request,'productos/productos.html', context)

@login_required
def agregar_producto(request):
  if request.method == 'GET':
    form = ProductFrom()
    context = {"form": form}
  elif request.method == 'POST':
    form = ProductFrom(request.POST)
    if (form.is_valid()):
      form.save()
      alert = create_alert("success", "El producto fue agregado correctamente!")
      form = ProductFrom()
    else:
      alert = {"type":"danger", "message":"Error al agregar el producto"}
    context = {"form": form, "alert":alert}
  return render(request, 'productos/formulario_producto.html' , context)

@login_required
def eliminar_producto(request,pk):
  if not (request.user.is_staff or request.user.is_authenticated):
    alert = create_alert("warning","Advertencia: No tienes permisos para realizar esta acción")
    request.session["alert"] = alert
    return redirect('ferreteria-productos')
  obj = Producto.objects.get(pk=pk)
  try:
    obj.delete()
  except Exception as e:
    alert = create_alert("error",f"Error al borrar objeto: {e}")
  alert = create_alert("success", "El producto fue eliminado con éxito!")
  request.session["alert"] = alert
  return redirect('ferreteria-productos')

@login_required
def editar_producto(request, pk):
  context={"editar":True}
  
  if not request.user.is_staff:
    request.session["alert"] = create_alert("warning","Advertencia: No tienes permisos para realizar esta acción")
    return redirect('ferreteria-productos')
  
  # Buscar objeto
  try:
    obj = Producto.objects.get(pk=pk)
  except Exception as e:
    request.session["alert"] = create_alert("danger",f"Error al buscar producto: {e}")
    return redirect('ferreteria-productos')
  
  if request.method == 'POST':
    form = ProductFrom(request.POST, instance=obj)
    if (form.is_valid()):
      form.save()
      alert = create_alert("success", "El producto fue editado correctamente!")
    else:
      alert = create_alert("danger", "error al editar producto...")
    context.update({"form":form, "alert":alert}) 
    return render(request,'productos/formulario_producto.html', context)
  
  form = ProductFrom(instance=obj)
  context.update({"form":form})
  return render(request, "productos/formulario_producto.html" , context)

# Vistas Auxiliares
from django.urls import reverse
def cambiar_moneda(request, new):
  request.session["moneda"] = new
  return redirect(request.GET.get('next','').strip(''))
