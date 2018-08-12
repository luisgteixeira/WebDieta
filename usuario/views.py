from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *

def cadastrar(request):
    if(request.method == 'POST'):
        form = FormularioCadastro(request.POST)

        if(form.is_valid()):
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return(redirect('/dashboard/'))
    else:
        form = FormularioCadastro()

    contexto = {'form' : form}
    return(render(request, 'registration/cadastrar.html', contexto))


@login_required(login_url='/login/')
def editar(request):
    if(request.method == 'POST'):
        form = FormularioEditar(request.POST)
        if(form.is_valid()):
            form.save(request.user)
            return(redirect('/dashboard/'))
    else:
        inicial = {'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'username': request.user.username,
                    'email': request.user.email
                }

        form = FormularioEditar(initial=inicial)

    return(render(request, 'registration/editar.html', {'form' : form}))
