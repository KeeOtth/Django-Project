from rest_framework import serializers
from .models import *

class CidadesSerializer(serializers.ModelSerializer):
    model = Cidades
    fields = '__all__'

class UfsSerializer(serializers.ModelSerializer):
    model = Ufs
    fields = '__all__'

class EnderecosSerializer(serializers.ModelSerializer):
    model = Enderecos
    fields = '__all__'
    
#Tá na hora do cocoricó, tá na hora da turma do Júlio! É o Júlio na gaita e a bicharada no cococoral cocoricóoooooo.

