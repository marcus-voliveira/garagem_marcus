from django.contrib import admin


from garagem_marcus.models import Marca
from garagem_marcus.models import Categoria
from garagem_marcus.models import Core
from garagem_marcus.models import Acessorio

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Core)
admin.site.register(Acessorio)


