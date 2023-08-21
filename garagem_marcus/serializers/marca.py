from rest_framework.serializers import ModelSerializer

from garagem_marcus.models import Marca

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer