from django.contrib.auth import authenticate
from django.shortcuts import render
from dieta.models import Info
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def dieta(request):
    return(render(request, 'dieta/dieta.html'))

@login_required(login_url='/login/')
def dashboard(request):
    return(render(request, 'dieta/dashboard.html'))
