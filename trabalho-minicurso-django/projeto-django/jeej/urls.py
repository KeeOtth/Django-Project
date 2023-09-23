from rest_framework import routers
from .views import *

routerJeej = routers.DefaultRouter()
routerJeej.register('cidades', CidadeView)
routerJeej.register('ufs', UfsView)
routerJeej.register('endereco', EnderecosView)