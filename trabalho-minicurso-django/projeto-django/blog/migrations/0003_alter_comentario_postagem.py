# Generated by Django 4.2.5 on 2023-09-21 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comentario_postagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='postagem',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.postagem'),
        ),
    ]
