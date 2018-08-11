from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .fusioncharts import FusionCharts
from django.http import HttpResponse
from collections import OrderedDict
from .forms import FormularioPeso
from dieta.models import *
import datetime

@login_required(login_url='/login/')
def dieta(request):
    return(render(request, 'dieta/dieta.html'))

@login_required(login_url='/login/')
def registrarPeso(request):
    if(request.method == 'POST'):
        form = FormularioPeso(request.POST)
        if(form.is_valid()):
            form.save(request.user)
            return(redirect('/dashboard/'))
    else:
        form = FormularioPeso()

    return(render(request, 'dieta/registrar-peso.html', {'form': form}))


@login_required(login_url='/login/')
def dashboard(request):
    usuario = request.user
    pesos = Peso.objects.filter(usuario_id=usuario.id).order_by('data_pesagem')
    graf = grafico(pesos)

    return(render(request, 'dieta/dashboard.html', graf))


def grafico(pesos):

    config_graf = OrderedDict()
    config_graf["caption"] = ""
    config_graf["subCaption"] = ""
    config_graf["xAxisName"] = "Peso"
    config_graf["yAxisName"] = "Quilograma (Kg)"
    config_graf["numberSuffix"] = ""
    config_graf["theme"] = "fusion"
    config_graf["displayStartIndex"] = "60"
    config_graf["displayEndIndex"] = "80"

    grafico = OrderedDict()
    grafico["chart"] = config_graf
    grafico["data"] = []

    for peso in pesos:
        dados = {}
        dados["label"] = peso.data_pesagem.strftime('%d/%m/%Y')
        dados["value"] = peso.peso
        grafico["data"].append(dados)

    grafico = FusionCharts("line", "ex1" , "60%", "55%", "chart-1", "json", grafico)

    return({'output' : grafico.render()})
