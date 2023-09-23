from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *

class CidadeView(viewsets.ModelViewSet):
    queryset = Cidades.objects.all()
    serializer_class = CidadesSerializer

class UfsView(viewsets.ModelViewSet):
    queryset = Ufs.objects.all()
    serializer_class = UfsSerializer

class EnderecosView(viewsets.ModelViewSet):
    queryset = Enderecos.objects.all()
    serializer_class = EnderecosSerializer


# Create your views here.
