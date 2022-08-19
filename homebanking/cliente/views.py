import locale

from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from cuentas.models import Cuenta
from .models import Cliente


@login_required()
def index(request: WSGIRequest) -> HttpResponse:
    """
    View function for Me Page of site.
    """
    locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')
    template_name: str = 'cliente/index.html'
    user = request.user
    costumer = Cliente.objects.get(user=user)
    main_account = Cuenta.objects.get(customer=user, type=Cuenta.AccountType.SAVINGS.value)

    try:
        us_account = Cuenta.objects.get(customer=user, type=Cuenta.AccountType.SAVINGS_USD.value)
    except Cuenta.DoesNotExist:
        us_account = None

    navbar: str = "navbar-light bg-light"
    navbar_text: str = ""
    log_out: str = "text-dark"

    if costumer.type == Cliente.CustomerType.GOLD.value:
        navbar = "navbar-light bg-gold"
        navbar_text = "Golden"
    elif costumer.type == Cliente.CustomerType.BLACK.value:
        navbar = "navbar-dark bg-dark"
        navbar_text = "Prestigious"
        log_out = "text-white"

    styles: dict = {
        "navbar": navbar,
        "navbar_text": navbar_text,
        "log_out": log_out,
        "account_balance": locale.currency(main_account.balance, grouping=True)
    }

    if us_account is not None:
        styles["us_balance"] = "US" + locale.currency(us_account.balance, grouping=True)
        styles["us_account"] = f"/ {us_account.iban}"

    context: dict = {
        "user": user,
        "costumer": costumer,
        "account": main_account,
        "styles": styles,
    }
    return render(request, template_name, context)
