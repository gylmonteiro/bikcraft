from django.db import models

# Create your models here.
class Bike(models.Model):
    modelo = models.CharField(max_length=30, verbose_name="Modelo da Bike")
    preco = models.FloatField(verbose_name='Preço')
    descricao = models.TextField(verbose_name='Descrição')
    foto = models.ImageField(upload_to='bikes/', blank=True, null=True)

    def __str__(self):
        return self.modelo


class Loja(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Nome')
    produtos = models.ManyToManyField(Bike)
    cnpj = models.CharField(max_length=25)
    detalhes = models.TextField()

    def __str__(self):
        return self.nome

class Vendedor(models.Model):
    nome = models.CharField(max_length=30, verbose_name="Nome")
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, verbose_name="Loja", related_name='vendedores')
    cpf = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome
    
