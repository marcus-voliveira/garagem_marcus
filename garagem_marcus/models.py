from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.nome.upper()
    
class Categoria(models.Model):
    veiculo = models.CharField(max_length=50)

    def __str__(self):
        return self.veiculo
    
                                     
