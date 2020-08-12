from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Client(models.Model):
    STATUS_CHOICES = (
        (1,"Persona Jurídica"),
        (2,"Persona Natural con Negocio"),
        (3,"Persona Natural sin Negocio"),
        )
    DOCUMENT_CHOICES = (
        (1,"RUC"),
        (2,"DNI"),
        )
    bussines_name = models.CharField("Razón Social", max_length=255)
    commercial_name = models.CharField("Nombre Comercial", max_length=255)
    website = models.URLField("Sitio Web", blank=True, null=True)
    email = models.EmailField("Correo", blank=True, null=True)
    type_person = models.IntegerField(choices=STATUS_CHOICES, default=1)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    addres = models.CharField("Dirección Fiscal", max_length=255)
    document_type = models.IntegerField(choices=DOCUMENT_CHOICES,default=1)
    number_document = models.CharField("Número de Documento", max_length=20, default="",
    blank=True, null=True)


    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.bussines_name}"

class Contact(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=("Cliente"))
    prefix = models.CharField("Prenombre", max_length=50, null=True, blank=True, default="")
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

class Bankaccount(models.Model):

    BANK_CHOICES = (
        (1,"BCP"),
        (2,"BBVA Continental"),
        (3,"Interbank"),
        (4,"BanBif"),
        (5,"MiBanco"),
        (6,"ScotiaBank"),
        (7,"Banco Falabella"),
        (8,"Banco Ripley"),
        (9,"Banco Azteca"),
        (10,"Banco Pichincha"),
        (11,"Banco de Comercio"),
        (12,"Banco Santander"),
        (13,"Banco GNB"),
        (14,"CRAC CAT Perú"),
        (15,"ICBC PERU BANK"),
    )

    ACCOUNT_CHOICES = (
        (1,"Crédito"),
        (2,"Débito"),
    )

    CURRENCY_CHOICES = (
        (1,"PEN"),
        (2,"USD"),
    )

    STATUS_CHOICES = (
        (1,"Activo"),
        (2,"Inactivo"),
        (3,"Otros"),
    )

    bank_id = models.IntegerField("Banco", choices=BANK_CHOICES, default=1)
    type_account = models.IntegerField("Tipo de Cuenta", choices=ACCOUNT_CHOICES)
    currency_id = models.IntegerField("Tipo de moneda", choices=CURRENCY_CHOICES)
    status = models.IntegerField("Estado", choices=STATUS_CHOICES)
    CCI_number = models.IntegerField("Cuenta Interbancaria")

    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'

    def __str__(self):
        return f"{self.bank_id}"
