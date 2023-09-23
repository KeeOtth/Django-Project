from django.db import models

class Professor(models.Model):
    id_professor = models.AutoField(primary_key=True)
    nome_professor = models.CharField(max_length=255)
    cpf_professor = models.CharField(max_length=11)
    rg_professor = models.CharField(max_length=8)
    codigo_professor = models.CharField(max_length=8)
    email_professor = models.EmailField(max_length=255)
    telefone_professor = models.CharField(max_length=11)

    class Meta:
        ordering = ['nome_professor']
        db_table = 'Professor'
        unique_together = ['nome_professor', 'cpf_professor', 'rg_professor']

class Disciplina(models.Model):
    id_disciplina = models.AutoField(primary_key=True)
    id_professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)
    nome_disciplina = models.CharField(max_length=255)
    cod_disciplina = models.CharField(max_length=7)
    carga_horaria_disciplina = models.IntegerField()
    ementa_disciplina = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['nome_disciplina']
        db_table = 'Disciplina'
        unique_together = ['nome_disciplina', 'cod_disciplina']    

class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome_aluno = models.CharField(max_length=255)
    cpf_aluno = models.CharField(max_length=11)
    rg_aluno = models.CharField(max_length=8)
    matricula_aluno = models.CharField(max_length=8)
    telefone_aluno = models.CharField(max_length=11)
    email_aluno = models.EmailField(max_length=255)

    class Meta:
        ordering = ['nome_aluno']
        db_table = 'Aluno'
        unique_together = ['nome_aluno', 'cpf_aluno', 'rg_aluno']

class Frequencia(models.Model):
    id_frequencia = models.AutoField(primary_key=True)
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    dia_frequencia = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Frequencia'

class FrequenciaAluno(models.Model):
    id_faluno = models.AutoField(primary_key=True)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    id_frequencia = models.ForeignKey(Frequencia, on_delete=models.CASCADE)
    presenca = models.BooleanField(default=True)

    class Meta:
        db_table = 'FrequenciaAluno'

class DisciplinaAluno(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nota = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['id_matricula', 'nota']
        db_table = 'Matricula'
        unique_together = ['id_matricula', 'id_aluno']

class PlanoAula(models.Model):
    id_plano_aula = models.AutoField(primary_key=True)
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    tema_aula = models.CharField(max_length=255)
    conteudo = models.TextField()
    metodo = models.CharField(max_length=50)
    dia_plano_aula = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'PlanoAula'

class Atividade(models.Model):
    id_atividade = models.AutoField(primary_key=True)
    atividade = models.TextField()
    tipo = models.CharField(max_length=50)
    data_postagem = models.DateField(auto_now_add=True)
    data_entrega = models.DateField(null=True, blank=True)
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    id_plano_aula = models.ForeignKey(PlanoAula, on_delete=models.CASCADE)

    class Meta:
        ordering = ['data_postagem']
        db_table = 'Atividade'

class AtividadeAluno(models.Model):
    id_atv_aluno = models.AutoField(primary_key=True)
    id_atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nota_atividade_aluno = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['id_aluno', 'nota_atividade_aluno']
        db_table = 'AtividadeAluno'
        unique_together = ['id_atv_aluno', 'id_atividade', 'id_aluno']