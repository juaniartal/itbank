from django.contrib.auth.models import User
from django.db import models


# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# Create your models here.
class Cliente(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE, unique=True)
    dni = models.IntegerField(null=True)
    dob = models.CharField(max_length=200, null=True)
    branch_id = models.IntegerField(null=True)
    direccion_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'CLIENTES'

    def __str__(self):
        return self.user.username
