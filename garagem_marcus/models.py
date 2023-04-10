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

class Acessorio(models.Model):
    descrição = models.CharField(max_length=100)

    def __str__(self):
        return self.descrição()
    
class Core(models.Model):
    descrição = models.CharField(max_length=100)

    def __str__(self):
        return self.descrição()    
    
class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="Veiculos")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="Veiculos")
    core = models.ForeignKey(Core, on_delete=models.PROTECT, related_name="Veiculos")
    ano = models.CharField(default= 0, max_length=4, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    

    def __str__(self):
        return f"{self.marca} {self.categoria} {self.core} {self.ano}"    

