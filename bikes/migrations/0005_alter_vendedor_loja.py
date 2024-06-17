# Generated by Django 5.0.6 on 2024-06-17 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0004_alter_loja_detalhes_alter_loja_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendedor',
            name='loja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendedores', to='bikes.loja', verbose_name='Loja atuante'),
        ),
    ]