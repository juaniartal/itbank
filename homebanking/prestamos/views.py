import locale

from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from cliente.models import Cliente
from .models import Prestamo


@login_required()
def index(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        return new_loan(request)
    locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')
    user = request.user
    customer = Cliente.objects.get(user=user)
    max_loan = Prestamo.get_max_loan(customer)
    loan_types = []
    for loan_type in Prestamo.LoanType.choices:
        loan_types.append({'value': loan_type[0], 'label': loan_type[1]})

    context: dict = {'user': user,
                     'customer': customer,
                     'max_loan': max_loan,
                     'loan_currency': locale.currency(max_loan, grouping=True),
                     'loan_types': loan_types,
                     }
    template_name: str = 'prestamos/prestamos.html'
    return render(request, template_name=template_name, context=context)


@login_required()
def new_loan(request: WSGIRequest) -> HttpResponse:
    return redirect('loans')
