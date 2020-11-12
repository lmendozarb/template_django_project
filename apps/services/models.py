from django.db import models


# Create your models here.
class Shipping(models.Model):
    SHIPPING_CHOICE = ((1, "Tarifa Plana"), (2, "Envio Gratis"), (3, "Recojo en Local"))
    zone_name = models.CharField("Nombre de Zona", max_length=250)
    # zone_region = models.ManytoManyField()
    shipping_method = models.IntegerField(choices=SHIPPING_CHOICE, default=1)

    class Meta:
        verbose_name = "Envío"
        verbose_name_plural = "Envíos"

    def __str__(self):
        return f"{self.zone_name}"


class ShippingConfigure(models.Model):
    enable_shipping_calculator = models.BooleanField("Habilitar Calculadora de Envío")
    hidden_shipping_prices = models.BooleanField("Ocultar Calculadora de Envío")

    class Meta:
        verbose_name = "Configuracion de Envío"
        verbose_name_plural = "Configuracion de Envíos"

    def __str__(self):
        return f"{self.enable_shipping_calculator}"
