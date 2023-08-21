from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem_marcus.models import Categoria
from garagem_marcus.serializers import CategoriaSerializer
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]