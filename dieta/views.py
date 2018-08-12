from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .fusioncharts import FusionCharts
from django.http import HttpResponse
from collections import OrderedDict
from .models import *
from .forms import *
import datetime

@login_required(login_url='/login/')
def dieta(request):

    form_refeicao = FormularioRefeicao()
    refeicoes = Refeicao.objects.filter(usuario_id=request.user.id).order_by('horario')

    if(request.method == 'POST'):
        if('data_inicio' in request.POST.keys()):
            form_info = FormularioInfo(request.POST)
            if(form_info.is_valid()):
                form_info.save(request.user)

        elif('tipo' in request.POST.keys()):
            form_refeicao = FormularioRefeicao(request.POST)
            if(form_refeicao.is_valid()):
                form_refeicao.save(request.user)
                return(redirect('dieta'))

    else:
        try:
            info = Info.objects.get(usuario_id=request.user.id)
            inicial = {'data_inicio': info.data_inicio, 'data_final': info.data_final, 'peso_ideal': info.peso_ideal, 'altura': info.altura}
        except Exception as e:
            inicial = {}

        form_info = FormularioInfo(initial=inicial)

    return(render(request, 'dieta/dieta.html', {'form_info': form_info, 'form_refeicao': form_refeicao, 'refeicoes': refeicoes}))


@login_required(login_url='/login/')
def registrarPeso(request):
    erro = ''
    if(request.method == 'POST'):
        form = FormularioPeso(request.POST)
        if(form.is_valid()):
            try:
                info = Info.objects.get(usuario_id=request.user.id)
                if(request.POST['data_pesagem'] >= info.data_inicio.strftime("%d/%m/%Y") and request.POST['data_pesagem'] <= info.data_final.strftime("%d/%m/%Y")):
                    form.save(request.user)
                    return(redirect('/dashboard/'))
                else:
                    erro = "Data de pesagem fora do intervalo de tempo da dieta"
            except:
                erro = "Nenhuma dieta foi cadastrada ainda"
    else:
        form = FormularioPeso()

    return(render(request, 'dieta/registrar-peso.html', {'form': form, 'erro': erro}))


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
