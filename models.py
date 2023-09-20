from django.db import models

class Ufs(models.Model):
    id_uf = models.AutoField(primary_key=True)
    nome_uf = models.CharField(max_length=30)
    sigla_uf = models.CharField(max_length=2)

class Cidades(models.Model):
    id_cidade = models.AutoField(primary_key=True)
    nome_cidade = models.CharField(max_length=50)
    id_uf = models.ForeignKey(Ufs)

class Enderecos(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    id_cidade = models.ForeignKey(Cidades)
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=8)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=80)
    complemento = models.CharField(max_length=60, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)

class Contas(models.Model):
    id_conta = models.AutoField(primary_key=True)
    TIPO_CONTA = [
        ('Poupança', 'Poupança'),
        ('Corrente', 'Corrente'),
    ]
    TIPO_BANCO = [
        ('Banco1', 'Banco1'),
        ('Banco2', 'Banco2'),
        ('Banco3', 'Banco3'),
        ('Banco4', 'Banco4'),
    ]
    tp_conta = models.CharField(choices=TIPO_CONTA, default="Poupança")
    id_banco = models.IntegerField()
    banco = models.CharField(choices=TIPO_BANCO, default="Banco1")
    conta = models.IntegerField()
    agencia = models.IntegerField()
    operacao = models.IntegerField()

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Pessoas(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    VINCULO_CHOICES = [
        ("Vinculo1", "Vinculo1"),
        ("Vinculo2", "Vinculo2"),
    ]
    vinculo_pessoa = models.CharField(choices=VINCULO_CHOICES, default='Vinculo1')
    id_user = models.ForeignKey(User)
    cpf_pessoa = models.IntegerField()
    nome_pessoa = models.CharField(max_length=200)
    telefone_pessoa = models.CharField(max_length=16)
    email_pessoa = models.EmailField()
    id_endereco = models.ForeignKey(Enderecos)
    id_conta = models.ForeignKey(Contas)
    
class Ocorrencias(models.Model):
    id_ocorrencia = models.AutoField(primary_key=True)
    data_ocorrencia = models.DateField(auto_now_add=True)
    realizada = models.BooleanField(default=True)
    ocorrencia = models.TextField()
    id_pessoa = models.ForeignKey(Pessoas)

    
