from django.contrib import admin

from .models import  Marca, Cor, Categoria, Acessorio, Veiculo

admin.site.register(Cor)
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Acessorio)
admin.site.register(Veiculo)




