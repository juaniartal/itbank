from django.contrib.auth.forms import UserCreationForm
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import RegisterForm


def index(request: WSGIRequest) -> HttpResponse:
    """
    View function for Login Page of site.
    """
    template_name: str = 'login/index.html'
    context: dict = {}
    return render(request, template_name, context)


def reset(request: WSGIRequest) -> HttpResponse:
    """
    View function for Reset Password Page of site.
    """
    template_name: str = 'login/reset.html'
    context: dict = {}
    return render(request, template_name, context)


def register(request: WSGIRequest) -> HttpResponse:
    """
    View function for Register Page of site.
    """
    template_name: str = 'login/register.html'
    form = RegisterForm()
    context: dict = {'form': form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, template_name, context)
