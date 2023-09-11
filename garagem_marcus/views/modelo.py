from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem_marcus.models import Modelo
from garagem_marcus.serializers import ModeloSerializer

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer