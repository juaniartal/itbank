from django.urls import path

from cuentas import views as account_views
from . import views

urlpatterns = [
    path('me', views.index, name='me'),
    path('me/accounts', account_views.index, name='my-accounts'),
]
