from django.contrib.admin.widgets import AdminDateWidget
from django.core.exceptions import ValidationError
from .models import Peso
from django import forms
import datetime


class FormularioPeso(forms.Form):
    peso = forms.FloatField(label='Peso')
    data_pesagem = forms.DateField(label='Data da pesagem', widget=AdminDateWidget)

    def clean_data_pesagem(self):
        data_pesagem = self.cleaned_data['data_pesagem']
        if(data_pesagem > datetime.datetime.now().date()):
            raise(ValidationError("Impossível selecionar uma data futura"))
        return(data_pesagem)

    def save(self, user, commit=True):
        peso = Peso.objects.create(
            usuario_id=user.id,
            peso=self.cleaned_data['peso'],
            data_pesagem=self.cleaned_data['data_pesagem']
        )
        return(peso)
