from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime


# Create your models here.


class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    class Meta:
        db_table = 'DIRECCIONES'



class Branch(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, default=None, )

    class Meta:
        db_table = 'SUCURSALES'



class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    dni = models.PositiveIntegerField(unique=True)
    hire_date = models.DateField(default=datetime.date.today)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, default=None)

    class Meta:
        db_table = 'EMPLEADOS'



class Cliente(models.Model):
    class CustomerType(models.TextChoices):
        CLASSIC = 'C', 'Classic'
        GOLD = 'G', 'Gold'
        BLACK = 'B', 'Black'

    id = models.IntegerField(primary_key=True,
                             editable=False,
                             null=False,
                             )
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE, unique=True)
    type = models.CharField(
        max_length=1,
        choices=CustomerType.choices,
        default=CustomerType.CLASSIC,
    )
    dni = models.IntegerField(null=True)
    dob = models.CharField(max_length=200, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, default=None, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, default=None)

    class Meta:
        db_table = 'CLIENTES'


class Cuenta(models.Model):
    class AccountType(models.TextChoices):
        CURRENT = 'CA', 'Current Account'
        SAVINGS = 'SA', 'Savings Account'
        SAVINGS_USD = 'SAU', 'Savings Account (USD)'

    id = models.CharField(primary_key=True,
                          max_length=10,
                          editable=False,
                          null=False, )
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=3,
        choices=AccountType.choices,
        default=AccountType.CURRENT,
    )
    iban = models.CharField(max_length=200,
                            null=True,
                            default="-",
                            )
    balance = models.FloatField(default=0.0)

    class Meta:
        db_table = 'CUENTAS'


class Prestamo(models.Model):
    class LoanType(models.TextChoices):
        MORTGAGE = 'MO', 'Mortgage'
        PERSONAL = 'PE', 'Personal'
        PLEDGE = 'PL', 'Pledge'

    id = models.IntegerField(primary_key=True, editable=False)
    customer = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=2,
        choices=LoanType.choices)
    date = models.DateField(default=datetime.datetime.now)
    total = models.FloatField()
    cancelled = models.FloatField(default=0.0)

    class Meta:
        db_table = 'PRESTAMOS'


class Tarjeta(models.Model):
    class CardType(models.TextChoices):
        DEBIT = 'D', 'Debit'
        CREDIT = 'C', 'Credit'
        GIFT = 'G', 'Gift'

    class CardBrand(models.TextChoices):
        VISA = 'VISA', "Visa"
        MASTERCARD = 'MASTERCARD', "Mastercard"
        AMEX = 'AMEX', "American Express"

    id = models.IntegerField(primary_key=True, editable=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=1,
        choices=CardType.choices,
        default=CardType.DEBIT
    )
    brand = models.CharField(
        max_length=25,
        choices=CardBrand.choices,
        default=CardBrand.VISA
    )
    number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=4)
    valid_from = models.DateField(auto_now=True, editable=False)
    expiration_end = models.DateField(editable=False)

    class Meta:
        unique_together = ('number', 'cvv')
        db_table = 'TARJETAS'                