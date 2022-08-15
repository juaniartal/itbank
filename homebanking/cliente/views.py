from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Cliente


@login_required()
def index(request: WSGIRequest) -> HttpResponse:
    """
    View function for Me Page of site.
    """
    template_name: str = 'cliente/index.html'
    user = request.user
    costumer = Cliente.objects.get(user=user)
    context: dict = {"user": user, "costumer": costumer}
    return render(request, template_name, context)
