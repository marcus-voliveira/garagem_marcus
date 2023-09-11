from django.db import models
from uploader.models import Image

from garagem_marcus.models import Categoria, Acessorio, Cor, Modelo

class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    descricao = models.CharField(max_length=50, null=True, blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="veiculos"
    )
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(null=True, blank=True)
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True
    )
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")
    
    capa = models.ManyToManyField(
        Image,
        related_name="+",
        #on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.marca} {self.categoria} {self.cor} {self.ano}"    