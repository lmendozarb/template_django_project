# Generated by Django 2.2.14 on 2020-08-10 20:11

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="RUC",
            field=models.CharField(default="", max_length=15, verbose_name="RUC"),
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "prefix",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=50,
                        null=True,
                        verbose_name="Prenombre",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, verbose_name="Nombre del Contacto"
                    ),
                ),
                (
                    "mobile_phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, verbose_name="Numero del movil"
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Correo")),
                (
                    "position",
                    models.CharField(blank=True, max_length=50, verbose_name="Cargo"),
                ),
                (
                    "info",
                    models.TextField(
                        blank=True, default="", null=True, verbose_name="Informacion"
                    ),
                ),
                (
                    "is_principal",
                    models.BooleanField(
                        default=False, verbose_name="Contacto Principal"
                    ),
                ),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clients.Client",
                        verbose_name="Cliente",
                    ),
                ),
            ],
            options={
                "verbose_name": "Contacto",
                "verbose_name_plural": "Contactos",
            },
        ),
    ]
