from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *

class ProfessorView(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class DisciplinaView(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class AlunoView(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class FrequenciaView(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer

class FrequenciaAlunoView(viewsets.ModelViewSet):
    queryset = FrequenciaAluno.objects.all()
    serializer_class = FrequenciaAlunoSerializer

class DisciplinaAlunoView(viewsets.ModelViewSet):
    queryset = DisciplinaAluno.objects.all()
    serializer_class = DisciplinaAlunoSerializer

class PlanoAulaView(viewsets.ModelViewSet):
    queryset = PlanoAula.objects.all()
    serializer_class = PlanoAulaSerializer

class AtividadeView(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer

class AtividadeAlunoView(viewsets.ModelViewSet):
    queryset = AtividadeAluno.objects.all()
    serializer_class = AtividadeAlunoSerializer