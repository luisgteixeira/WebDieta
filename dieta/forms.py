from django.core.exceptions import ValidationError
from .models import *
from django import forms
import datetime


class FormularioPeso(forms.Form):
    peso = forms.FloatField(label='Peso')
    data_pesagem = forms.DateField(label='Data da pesagem')

    def clean_data_pesagem(self):
        data_pesagem = self.cleaned_data['data_pesagem']
        if(data_pesagem > datetime.datetime.now().date()):
            raise(ValidationError("Impossível selecionar uma data futura"))
        return(data_pesagem)

    def save(self, usuario, commit=True):
        peso = Peso.objects.create(
            usuario_id=usuario.id,
            peso=self.cleaned_data['peso'],
            data_pesagem=self.cleaned_data['data_pesagem']
        )
        return(peso)


class FormularioInfo(forms.Form):
    data_inicio = forms.DateField(label='Data de Início')
    data_final = forms.DateField(label='Data Final')
    peso_ideal = forms.FloatField(label='Peso Ideal')
    altura = forms.FloatField(label='Altura')

    def save(self, usuario, commit=True):
        info = Info.objects.get(usuario_id=usuario.id)
        if(info is None):
            info = Info.objects.create(
                usuario_id=usuario.id,
                data_inicio=self.cleaned_data['data_inicio'],
                data_final=self.cleaned_data['data_final'],
                peso_ideal=self.cleaned_data['peso_ideal'],
                altura=self.cleaned_data['altura']
            )
        else:
            info = Info.objects.update(
                data_inicio=self.cleaned_data['data_inicio'],
                data_final=self.cleaned_data['data_final'],
                peso_ideal=self.cleaned_data['peso_ideal'],
                altura=self.cleaned_data['altura']
            )
        return(info)


class FormularioRefeicao(forms.Form):
    TIPOS_OPCOES = (
        ('CAFE_MANHA', 'Café da Manhã'),
        ('LANCHE', 'Lanche'),
        ('ALMOCO', 'Almoço'),
        ('JANTAR', 'Jantar'),
        ('CEIA', 'Ceia'),
    )
    tipo = forms.ChoiceField(choices=TIPOS_OPCOES, label='Refeição')
    horario = forms.TimeField(label='Horário')
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea)

    def save(self, usuario, commit=True):
        refeicao = Refeicao.objects.create(
            usuario_id=usuario.id,
            tipo=self.cleaned_data['tipo'],
            horario=self.cleaned_data['horario'],
            descricao=self.cleaned_data['descricao']
        )
        return(refeicao)
