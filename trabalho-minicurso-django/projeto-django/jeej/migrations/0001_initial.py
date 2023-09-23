# Generated by Django 4.2.5 on 2023-09-21 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidades',
            fields=[
                ('id_cidade', models.AutoField(primary_key=True, serialize=False)),
                ('nome_cidade', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Cidades',
                'ordering': ['nome_cidade'],
            },
        ),
        migrations.CreateModel(
            name='Contas',
            fields=[
                ('id_conta', models.AutoField(primary_key=True, serialize=False)),
                ('tp_conta', models.CharField(choices=[('Poupança', 'Poupança'), ('Corrente', 'Corrente')], default='Poupança', max_length=30)),
                ('id_banco', models.IntegerField()),
                ('banco', models.CharField(choices=[('Banco1', 'Banco1'), ('Banco2', 'Banco2'), ('Banco3', 'Banco3'), ('Banco4', 'Banco4')], default='Banco1', max_length=30)),
                ('conta', models.IntegerField()),
                ('agencia', models.IntegerField()),
                ('operacao', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Enderecos',
            fields=[
                ('id_endereco', models.AutoField(primary_key=True, serialize=False)),
                ('logradouro', models.CharField(max_length=150)),
                ('numero', models.CharField(max_length=8)),
                ('cep', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=80)),
                ('complemento', models.CharField(blank=True, max_length=60, null=True)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('id_cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jeej.cidades')),
            ],
            options={
                'db_table': 'Enderecos',
                'ordering': ['logradouro', 'bairro', 'numero', 'cep'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ufs',
            fields=[
                ('id_uf', models.AutoField(primary_key=True, serialize=False)),
                ('nome_uf', models.CharField(max_length=30)),
                ('sigla_uf', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'Ufs',
                'ordering': ['nome_uf'],
                'unique_together': {('nome_uf', 'sigla_uf')},
            },
        ),
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id_pessoa', models.AutoField(primary_key=True, serialize=False)),
                ('vinculo_pessoa', models.CharField(choices=[('Vinculo1', 'Vinculo1'), ('Vinculo2', 'Vinculo2')], default='Vinculo1', max_length=30)),
                ('cpf_pessoa', models.IntegerField()),
                ('nome_pessoa', models.CharField(max_length=200)),
                ('telefone_pessoa', models.CharField(max_length=16)),
                ('email_pessoa', models.EmailField(max_length=254)),
                ('id_conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jeej.contas')),
                ('id_endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jeej.enderecos')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jeej.user')),
            ],
        ),
        migrations.CreateModel(
            name='Ocorrencias',
            fields=[
                ('id_ocorrencia', models.AutoField(primary_key=True, serialize=False)),
                ('data_ocorrencia', models.DateField(auto_now_add=True)),
                ('realizada', models.BooleanField(default=True)),
                ('ocorrencia', models.TextField()),
                ('id_pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jeej.pessoas')),
            ],
        ),
        migrations.AddField(
            model_name='cidades',
            name='id_uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jeej.ufs'),
        ),
        migrations.AlterUniqueTogether(
            name='cidades',
            unique_together={('nome_cidade', 'id_uf')},
        ),
    ]