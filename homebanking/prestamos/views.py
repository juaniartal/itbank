from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from cliente.models import Cliente
from .models import Prestamo


@login_required()
def index(request: WSGIRequest) -> HttpResponse:
    user = request.user
    costumer = Cliente.objects.get(user=user)
    context: dict = {'user': user, 'costumer': costumer, 'max_loan': Prestamo.get_max_loan(costumer)}
    template_name: str = 'prestamos/prestamos.html'
    return render(request, template_name=template_name, context=context)
