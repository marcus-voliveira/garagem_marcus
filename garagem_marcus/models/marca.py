from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Marcas"