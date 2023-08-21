from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem_marcus.models import Marca
from garagem_marcus.serializers import MarcaSerializer
class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer