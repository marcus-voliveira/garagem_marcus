from rest_framework.serializers import ModelSerializer

from garagem_marcus.models import Acessorio
class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"