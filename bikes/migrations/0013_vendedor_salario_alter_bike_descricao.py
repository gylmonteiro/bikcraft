# Generated by Django 5.0.6 on 2024-09-03 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0012_bikeinventario'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='salario',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bike',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
    ]
