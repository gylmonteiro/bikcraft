# Generated by Django 5.0.6 on 2024-08-31 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0011_delete_bikeinventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeInventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_bikes', models.IntegerField()),
                ('valor_total_de_bikes', models.FloatField()),
                ('data_do_inventario', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-data_do_inventario'],
            },
        ),
    ]
