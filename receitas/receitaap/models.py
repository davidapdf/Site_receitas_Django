from django.db import models
from datetime import datetime

class Receitas(models.Model):
    nome_receita = models.CharField(max_length =200)
    ingredientes = models.TextField()
    mode_de_preparo = models.TextField()
    tempo_de_preparo = models.IntegerField()
    rendimento = models.TextField(max_length= 100)
    categoria = models.CharField(max_length = 100)
    data_receite = models.DateField(default = datetime.now, blank = True)

