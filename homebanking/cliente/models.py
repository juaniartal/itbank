from django.contrib.auth.models import User
from django.db import models


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
