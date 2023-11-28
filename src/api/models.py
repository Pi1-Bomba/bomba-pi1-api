from django.db import models

class Lancamento(models.Model):
    idFoguete = models.BigIntegerField()
    volume = models.FloatField(),
    peso = models.FloatField(),
    angulo = models.FloatField(),
    pressao = models.FloatField()

    def __str__(self):
        return self.idFoguete