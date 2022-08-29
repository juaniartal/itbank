from django.urls import path
from . import views

urlpatterns = [
    path('tarjetas/<int:idCliente>/', views.Tarjetas.as_view()),
]