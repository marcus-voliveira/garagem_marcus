from django.db import models

class Categoria(models.Model):
    veiculo = models.CharField(max_length=50)

    def __str__(self):
        return self.veiculo