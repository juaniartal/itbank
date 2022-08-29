from django.urls import path
from . import views

urlpatterns = [
    path('tarjetas/<int:cliente_id>/', views.Tarjetas.as_view()),
]