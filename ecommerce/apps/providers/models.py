from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Providers(models.Model):
    DNI = 1
    RUC = 2
    DOCUMENT_CHOICES = (
        (DNI,"DNI"),
        (RUC,"RUC"),
        )

    business_name = models.CharField("Razón Social", max_length=255)
    document_type = models.IntegerField("Tipo de Documento",
    choices=DOCUMENT_CHOICES, default=DNI)
    nr_document = models.CharField("Número de Documento", max_length=20,
    default="", blank=True, null=True)
    adress = models.CharField(max_length=255)
    phone = PhoneNumberField("Número del Movil")
    email = models.EmailField("Correo")
    website = models.URLField("Sitio Web", blank=True, null=True)
    favorite_provider = models.BooleanField()
    info = models.TextField()

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return f"{self.business_name}"

class ProvidersContact(models.Model):
    provider = models.ForeignKey(Providers, on_delete=models.CASCADE,
    verbose_name=("Proveedor"))
    name = models.CharField("Nombre del Contacto", max_length=255)
    mobile_phone = PhoneNumberField("Número del Movil")
    email = models.EmailField("Correo")
    position = models.CharField("Posicion", max_length=255)
    info = models.TextField()
    is_principal = models.CharField("Principal", max_length=255)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return f"{self.name}"
