from django.db import models

class Postagem(models.Model):
    id_postagem = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    data = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['data', 'titulo']
        db_table = 'Abacaxi'
        unique_together = ['data', 'titulo']

class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key = True)
    comentario = models.TextField()
    data = models.DateField(auto_now_add=True)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    