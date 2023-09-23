from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *

class PostagemView(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer

    @action(detail=True, methods = ['get'])
    def data_postagem(self, request, pk=None):
        postagem = Postagem.objects.get(id_postagem=pk)
        return Response(postagem.data)