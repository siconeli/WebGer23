# Generated by Django 4.2.5 on 2023-10-19 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditoria',
            name='acao',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='auditoria',
            name='tipo_objeto',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='auditoria',
            name='view',
            field=models.CharField(max_length=255),
        ),
    ]