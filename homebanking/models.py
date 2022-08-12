# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    dni = models.IntegerField()
    dob = models.CharField(max_length=200)
    branch_id = models.IntegerField()
    direccion_id = models.IntegerField()

    class Meta:
       managed = False
       db_table = 'CLIENTES'

class Cuenta(models.Model):
    id = models.IntegerField(primary_key=True)
    cliente_id = models.IntegerField() 
    balance = models.IntegerField()
    iban = models.CharField(max_length=200)
    tipo_cuenta_id = models.IntegerField()
    
    class Meta:
       managed = False
       db_table = 'CUENTAS'
        
     
class Empleado(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    hire_date = models.DateTimeField(auto_now=True)
    dni = models.IntegerField()
    branch_id = models.IntegerField()
    direccion_id = models.ForeignKey()
    
    
    class Meta:
        managed = False
        db_table = 'EMPLEADOS'

        
class Prestamo(models, Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'PRESTAMO'        
