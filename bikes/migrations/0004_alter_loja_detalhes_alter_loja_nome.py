# Generated by Django 5.0.6 on 2024-06-13 20:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0003_vendedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loja',
            name='detalhes',
            field=models.TextField(default=datetime.datetime(2024, 6, 13, 20, 11, 41, 421726, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loja',
            name='nome',
            field=models.CharField(max_length=30, verbose_name='Nome'),
        ),
    ]