from django.db import models

# Create your models here.
class Bike(models.Model):
    modelo = models.CharField(max_length=30, verbose_name="Modelo da Bike")
    preco = models.FloatField(verbose_name='Preço')
    descricao = models.TextField(verbose_name='Descrição')
    foto = models.ImageField(upload_to='bikes/', blank=True, null=True)

    def __str__(self):
        return self.modelo

