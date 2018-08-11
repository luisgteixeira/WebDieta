from django.urls import path
from . import views

urlpatterns = [
    path('dieta/', views.dieta, name='dieta'),
    path('registrar-peso/', views.registrarPeso, name="registrarPeso"),
    path('dashboard/', views.dashboard, name='dashboard')
]
