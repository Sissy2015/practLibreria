from django.shortcuts import redirect, render

from administrador.form import CategoriaForms
from administrador.models import categoria

# Create your views here.
#def home(request):
#    return render(request,'administrador/template.html',{})

def listadoCateg(request):
  arreglo = {}
  arreglo['lista']=categoria.objects.all()
  return render(request,'administrador/listadoCategorias.html',arreglo)

def RegistrarCateg(request):
  arreglo = {}
  if(request.method=="POST"):
    form=CategoriaForms(request.POST)
    if form.is_valid():
      form.save()
      return redirect('categorias')
  else:
    auxC=categoria()
    form=CategoriaForms(None)  
  arreglo['form']=form
  return render(request,'administrador/frmRegCategorias.html',arreglo)
