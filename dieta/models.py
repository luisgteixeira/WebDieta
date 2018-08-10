from django.db import models
from django.conf import settings

class Info(models.Model):
    id_dieta = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    data_inicio = models.DateField()
    data_final = models.DateField()
    peso_ideal = models.FloatField()
    altura = models.FloatField()

    def __str__(self):
        return self.usuario.username

class Peso(models.Model):
    id_peso = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    peso = models.FloatField()
    data_pesagem = models.DateField()

    def __str__(self):
        return self.usuario.username


class Refeicao(models.Model):
    id_refeicao = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    TIPOS_OPCOES = (
        ('CAFE_MANHA', 'Café da Manhã'),
        ('LANCHE', 'Lanche'),
        ('ALMOCO', 'Almoço'),
        ('JANTAR', 'Jantar'),
        ('CEIA', 'Ceia'),
    )

    tipo = models.CharField(
        max_length=10,
        choices=TIPOS_OPCOES,
        default='CAFE_MANHA',
    )
    horario = models.TimeField()
    descricao = models.TextField()

    def __str__(self):
        return self.usuario.username
