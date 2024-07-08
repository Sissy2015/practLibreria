from django.urls import path
from .import views

urlpatterns = [
    #path('home/',views.home,name='home'),
    path('categoria/',views.listadoCateg,name='categorias'),
    path('registrarcategoria/',views.RegistrarCateg,name='RegistrarCategorias'),
]