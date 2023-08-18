from django.db import models

class Veiculo(models.Model):
    descricao = models.CharField(max_length=50, null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="veiculos"
    )
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(null=True, blank=True)
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True
    )
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")

    def __str__(self):
        return f"{self.marca} {self.categoria} {self.cor} {self.ano}"    