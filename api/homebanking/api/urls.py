from django.urls import path
from . import views

urlpatterns = [
    path('clientes/<int:cliente_id>/', views.Clientes.as_view()),
    path('cuentas/<int:cliente_id>/', views.Cuentas.as_view()),
    path('prestamos/<int:cliente_id>/', views.Prestamos.as_view()), 
    path('prestamosSucursal/<int:branch_id>/', views.PrestamosSucursal.as_view()),     
    path('tarjetas/<int:cliente_id>/', views.Tarjetas.as_view()),
    path('sucursales/', views.Sucursales.as_view()),     
]