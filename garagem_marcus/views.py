from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from garagem_marcus.models import Marca, Categoria, Cor, Acessorio, Veiculo 
from garagem_marcus.serializers import MarcaSerializer, CategoriaSerializer, CorSerializer, AcessorioSerializer, VeiculoSerializer, VeiculoDetailSerializer, VeiculoListSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    
    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer