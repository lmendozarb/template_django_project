from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Client(models.Model):
    STATUS_CHOICES = (
        (1,"Persona Jurídica"),
        (2,"Persona Natural con Negocio"),
        (3,"Persona Natural sin Negocio"),
    )
    bussines_name = models.CharField("Razón Social", max_length=255)
    commercial_name = models.CharField("Nombre Comercial", max_length=255)
    website = models.URLField("Sitio Web", blank=True, null=True)
    email = models.EmailField("Correo", blank=True, null=True)
    type_person = models.IntegerField(choices=STATUS_CHOICES)
    addres = models.CharField("Dirección Fiscal", max_length=255)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.bussines_name}"

class Contact(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=("Cliente"))
    name = models.CharField("Nombre del Contacto", max_length=255)
    mobile_phone = PhoneNumberField("Numero del movil")
    email = models.EmailField("Correo")
    position = models.CharField("Cargo", max_length=50, blank=True)
    info = models.TextField("Informacion", default="", blank=True, null=True)
    is_principal = models.BooleanField("Contacto Principal", default=False)


    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return f"{self.name}"
