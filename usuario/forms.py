from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms


class FormularioCadastro(forms.Form):
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    username = forms.CharField(label='Usuário', min_length=4, max_length=150)
    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label='Digite sua senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme sua senha', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Nome de usuário já cadastrado")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("E-mail já cadastrado")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Senhas não são iguais")

        return password2

    def save(self, commit=True):
        usuario = User.objects.create_user(
            self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )
        return(usuario)

class FormularioEditar(forms.Form):
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')

    def save(self, commit=True):
        usuario = User.objects.update(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )

        return(usuario)
