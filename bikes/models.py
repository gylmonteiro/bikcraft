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
    salario = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return self.nome


class BikeInventario(models.Model):
    numero_de_bikes = models.IntegerField()
    valor_total_de_bikes = models.FloatField()
    data_do_inventario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-data_do_inventario"]

    def __str__(self):
        return f'Nº de Bikes {self.numero_de_bikes} | Valor total R$ {self.valor_total_de_bikes}'
    
