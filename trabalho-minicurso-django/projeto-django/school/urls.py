from rest_framework import routers
from .views import *

routerSchool = routers.DefaultRouter()
routerSchool.register(r'professor', ProfessorView)
routerSchool.register(r'disciplina', DisciplinaView)
routerSchool.register(r'disciplina_aluno', DisciplinaAlunoView)
routerSchool.register(r'aluno', AlunoView)
routerSchool.register(r'frequencia', FrequenciaView)
routerSchool.register(r'frequencia_aluno', FrequenciaAlunoView)
routerSchool.register(r'plano_aula', PlanoAulaView)
routerSchool.register(r'atividade', AtividadeView)
routerSchool.register(r'atividade_aluno', AtividadeAlunoView)