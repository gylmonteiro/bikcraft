from django.db import models

# Create your models here.
class Bike(models.Model):
    modelo = models.CharField(max_length=30)
    preco = models.FloatField()
    descricao = models.TextField()
    foto = models.ImageField(upload_to='bikes/', blank=True, null=True)

    def __str__(self):
        return self.modelo

