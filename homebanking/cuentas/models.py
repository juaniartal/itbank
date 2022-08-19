import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from schwifty import IBAN

from cliente.models import Cliente


# Create your models here.

class Cuenta(models.Model):
    class AccountType(models.TextChoices):
        CURRENT = 'CA', 'Current Account'
        SAVINGS = 'SA', 'Savings Account'
        SAVINGS_USD = 'SAU', 'Savings Account (USD)'

    id = models.CharField(primary_key=True,
                          default=str(uuid.uuid4().int)[:10],
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

    def __str__(self):
        return f"{self.iban} - {self.get_type_display()}"


@receiver(post_save, sender=Cuenta)
def populate_iban(sender, instance, created, **kwargs):
    if created:
        data = Cuenta.objects.get(id=instance.id)
        data.iban = str(IBAN.generate('DE', bank_code='10001138', account_code=str(data.id)))
        data.save()


@receiver(post_save, sender=Cliente)
def create_account_for_costumer(sender, instance, created, **kwargs):
    if created:
        customer = instance.user
        account = Cuenta(id=str(uuid.uuid4().int)[:10], customer=customer, type=Cuenta.AccountType.SAVINGS.value)
        account.save()
        match instance.type:
            case instance.CustomerType.GOLD:
                account_1 = Cuenta(id=str(uuid.uuid4().int)[:10], customer=customer,
                                   type=Cuenta.AccountType.SAVINGS_USD.value)
                account_1.save()
            case instance.CustomerType.BLACK:
                account_2 = Cuenta(id=str(uuid.uuid4().int)[:10], customer=customer,
                                   type=Cuenta.AccountType.SAVINGS_USD.value)
                account_2.save()
                account_3 = Cuenta(id=str(uuid.uuid4().int)[:10], customer=customer,
                                   type=Cuenta.AccountType.CURRENT.value)
                account_3.save()
