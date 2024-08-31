from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from .models import Bike, BikeInventario


@receiver(post_save, sender=Bike)
def bike_post_save(sender, instance, **kwargs):
    numero_de_bikes = Bike.objects.all().count()
    valor_total_de_bikes = Bike.objects.aggregate(valor_total=Sum("preco"))[
        "valor_total"
    ]

    BikeInventario.objects.create(
        numero_de_bikes=numero_de_bikes, valor_total_de_bikes=valor_total_de_bikes
    )

@receiver (post_delete, sender=Bike)
def bike_post_delete(sender, instance, **kwargs):
    numero_de_bikes = Bike.objects.all().count()
    valor_total_de_bikes = Bike.objects.aggregate(valor_total=Sum("preco"))[
        "valor_total"
    ]

    BikeInventario.objects.create(
        numero_de_bikes=numero_de_bikes, valor_total_de_bikes=valor_total_de_bikes
    )
