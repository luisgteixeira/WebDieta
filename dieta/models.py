from django.db import models

class Info(models.Model):
    id_dieta = models.AutoField(primary_key=True)
    # usuario = models.ForeignKey()
    inicio = models.DateField()
    final = models.DateField()
    peso_ideal = models.FloatField()
    altura = models.FloatField()

class Peso(models.Model):
    id_peso = models.AutoField(primary_key=True)
    dieta_peso = models.ForeignKey('Info', on_delete=models.DO_NOTHING)
    peso = models.FloatField()
    data_pesagem = models.DateField()


class Refeicao(models.Model):
    id_refeicao = models.AutoField(primary_key=True)
    refeicao_dieta = models.ForeignKey('Info', on_delete=models.DO_NOTHING)
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
