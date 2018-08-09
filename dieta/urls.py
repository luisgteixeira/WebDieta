from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('dieta/', views.dieta)
]
