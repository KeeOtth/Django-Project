# Generated by Django 4.2.5 on 2023-09-21 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comentario_postagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='postagem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.postagem'),
        ),
    ]
