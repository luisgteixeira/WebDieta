from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import FormularioCadastro

def cadastrar(request):
    if request.method == 'POST':
        form = FormularioCadastro(request.POST)

        if form.is_valid():
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
