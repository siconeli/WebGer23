# Generated by Django 4.2.3 on 2023-10-08 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessoAdm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True, verbose_name='data_criação')),
                ('data_alteracao', models.DateField(auto_now=True, verbose_name='Alterado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('numero', models.CharField(max_length=10, unique=True, verbose_name='N°')),
                ('municipio', models.CharField(max_length=50, verbose_name='Município')),
                ('uf', models.CharField(max_length=2)),
                ('data_inicial', models.DateField(blank=True, null=True)),
                ('data_final', models.DateField(blank=True, null=True)),
                ('data_div_ativa', models.DateField(blank=True, null=True)),
                ('valor_atributo', models.CharField(blank=True, max_length=14, null=True)),
                ('valor_multa', models.CharField(blank=True, max_length=14, null=True)),
                ('valor_credito', models.CharField(blank=True, max_length=14, null=True)),
                ('valor_atualizado', models.CharField(blank=True, max_length=14, null=True)),
                ('data_valor_atualizado', models.DateField(blank=True, null=True)),
                ('nome_contribuinte', models.CharField(max_length=50)),
                ('tipo_pessoa', models.CharField(choices=[('Física', 'Física'), ('Jurídica', 'Jurídica')], max_length=50)),
                ('documento', models.CharField(max_length=20, unique=True, verbose_name='CPF/CNPJ')),
                ('nome_fantasia', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('endereco', models.CharField(max_length=150)),
                ('complemento', models.CharField(blank=True, max_length=50, null=True)),
                ('municipio_contribuinte', models.CharField(blank=True, max_length=50, null=True)),
                ('uf_contribuinte', models.CharField(blank=True, max_length=2, null=True, verbose_name='UF')),
                ('cep', models.CharField(blank=True, max_length=10, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TipoAndamentoAdm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True, verbose_name='data_criação')),
                ('data_alteracao', models.DateField(auto_now=True, verbose_name='Alterado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('tipo_andamento', models.CharField(max_length=100, verbose_name='Tipo de Andamento')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Auditoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_model', models.CharField(max_length=255)),
                ('id_novo_registro', models.PositiveIntegerField()),
                ('acao', models.CharField(max_length=10)),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-data_hora',),
            },
        ),
        migrations.CreateModel(
            name='AndamentoAdm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True, verbose_name='data_criação')),
                ('data_alteracao', models.DateField(auto_now=True, verbose_name='Alterado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('data_andamento', models.DateField(verbose_name='Data do Andamento')),
                ('situacao_pagamento', models.CharField(blank=True, choices=[('Sem Pagamento', 'Sem Pagamento'), ('Com Pagamento', 'Com Pagamento')], max_length=100, null=True)),
                ('valor_pago', models.CharField(blank=True, max_length=14, null=True)),
                ('data_prazo', models.DateField(blank=True, null=True)),
                ('funcionario', models.CharField(blank=True, max_length=50, null=True)),
                ('data_recebimento', models.DateField(blank=True, null=True)),
                ('complemento', models.CharField(blank=True, max_length=150, null=True)),
                ('arquivo', models.FileField(blank=True, upload_to='Arquivo/', verbose_name='Arquivo')),
                ('criador_andamento_adm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário Criador')),
                ('processo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processo.processoadm')),
                ('tipo_andamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processo.tipoandamentoadm')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
