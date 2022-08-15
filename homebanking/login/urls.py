from django.urls import path

from . import views

urlpatterns = [
    path('login', views.index, name='login'),
    path('reset', views.reset, name='reset_password'),
]
