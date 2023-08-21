from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem_marcus.models import Cor
from garagem_marcus.serializers import CorSerializer
class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer