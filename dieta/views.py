from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.http import HttpResponse
from collections import OrderedDict
from django.shortcuts import render
from dieta.models import *
from .fusioncharts import FusionCharts
import datetime

@login_required(login_url='/login/')
def dieta(request):
    return(render(request, 'dieta/dieta.html'))


@login_required(login_url='/login/')
def dashboard(request):
    usuario = request.user
    pesos = Peso.objects.filter(usuario_id=usuario.id)
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

    grafico = FusionCharts("line", "ex1" , "60%", "50%", "chart-1", "json", grafico)

    return({'output' : grafico.render()})
