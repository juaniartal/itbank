from django.urls import path
from . import views

urlpatterns = [
    path('clientes/<int:cliente_id>/', views.Clientes.as_view()),
    path('tarjetas/<int:cliente_id>/', views.Tarjetas.as_view()),
]