from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=120)
    sigla = models.CharField(max_length=5)
    descricao = models.TextField()
