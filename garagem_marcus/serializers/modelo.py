from rest_framework.serializers import ModelSerializer

from garagem_marcus.models import Modelo

class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"
        depth = 1