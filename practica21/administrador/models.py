from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class categoria(models.Model):
    id= models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=150)

class libro(models.Model):
    id= models.AutoField(primary_key=True)
    autor=models.CharField(max_length=255)
    editorial=models.CharField(max_length=100)
    aniopublicacion=models.IntegerField(default=2024)
    titulo=models.CharField(max_length=255)
    precio=models.FloatField(max_length=100)
    imagen=models.ImageField(upload_to="administrador/img",null=True)
    stock= models.IntegerField(default=0)
    idcategoria = models.ForeignKey(categoria,on_delete=models.CASCADE,null= True)

class cliente(models.Model):
    id= models.AutoField(primary_key=True)
    cedula=models.CharField(max_length=10,default="")
    direccion = models.CharField(max_length=50,default="")
    id_user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)

class factura(models.Model):
    id= models.AutoField(primary_key=True)
    fecha=models.DateField(auto_now=NULL)
    iva=models.FloatField(default=0.0)
    nrofactura=models.CharField(max_length=20,default="")
    subtotal=models.FloatField(default=0.0)
    total=models.FloatField(default=0.0)
    idcliente= models.ForeignKey(cliente,on_delete=models.CASCADE,null= True)

class detallefactura(models.Model):
    id= models.AutoField(primary_key=True)
    precioTotal=models.FloatField(default=0.0)
    precioUnitario=models.FloatField(default=0.0)
    idfactura= models.ForeignKey(factura,on_delete=models.CASCADE,null= True)
    idlibro=models.ForeignKey(libro,on_delete=models.CASCADE,null= True)


