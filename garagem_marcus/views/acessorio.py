from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem_marcus.models import Acessorio
from garagem_marcus.serializers import AcessorioSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer