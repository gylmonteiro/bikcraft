# Generated by Django 5.0.6 on 2024-06-04 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=30)),
                ('preco', models.FloatField()),
                ('descricao', models.TextField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='bikes/')),
            ],
        ),
    ]