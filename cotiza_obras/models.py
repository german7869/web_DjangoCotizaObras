from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField()

class Cotizacion(models.Model):
    fecha_emision =  models.DateField()
    numero = models.AutoField(primary_key=True)
    id_cliente =  models.ForeignKey(Cliente, on_delete=models.CASCADE)
    subtotal = models.FloatField()
    costo_obra = models.FloatField()
    porcentaje_utilidad = models.FloatField()
    total = models.FloatField()

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    descripcion = models.CharField()
    
class Material(models.Model):
    id_mateiral = models.AutoField(primary_key=True)
    descripcion = models.CharField()
    costo = models.FloatField()

class Detalle_productos(models.Model):
    id_detalle_prodcuto = models.AutoField(primary_key=True)
    id_cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    porcentaje_utilidad = models.FloatField()
    costo_material = models.FloatField()
    precio = models.FloatField()
    valor = models.FloatField()
    costo_total = models.FloatField()

class Detalle_mateirales(models.Model):
    id_detalle_material = models.AutoField(primary_key=True)
    id_cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    costo_material = models.FloatField()
    alto = models.FloatField()
    ancho = models.FloatField()
    valor = models.FloatField()


    
