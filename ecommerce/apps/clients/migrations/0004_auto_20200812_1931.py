# Generated by Django 2.2.14 on 2020-08-12 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0003_bankaccount"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="client",
            name="RUC",
        ),
        migrations.AddField(
            model_name="client",
            name="document_type",
            field=models.IntegerField(choices=[(1, "RUC"), (2, "DNI")], default=1),
        ),
        migrations.AddField(
            model_name="client",
            name="number_document",
            field=models.CharField(
                blank=True,
                default="",
                max_length=20,
                null=True,
                verbose_name="Número de Documento",
            ),
        ),
        migrations.AlterField(
            model_name="bankaccount",
            name="CCI_number",
            field=models.IntegerField(verbose_name="Cuenta Interbancaria"),
        ),
        migrations.AlterField(
            model_name="bankaccount",
            name="bank_id",
            field=models.IntegerField(
                choices=[
                    (1, "BCP"),
                    (2, "BBVA Continental"),
                    (3, "Interbank"),
                    (4, "BanBif"),
                    (5, "MiBanco"),
                    (6, "ScotiaBank"),
                    (7, "Banco Falabella"),
                    (8, "Banco Ripley"),
                    (9, "Banco Azteca"),
                    (10, "Banco Pichincha"),
                    (11, "Banco de Comercio"),
                    (12, "Banco Santander"),
                    (13, "Banco GNB"),
                    (14, "CRAC CAT Perú"),
                    (15, "ICBC PERU BANK"),
                ],
                default=1,
                verbose_name="Banco",
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="type_person",
            field=models.IntegerField(
                choices=[
                    (1, "Persona Jurídica"),
                    (2, "Persona Natural con Negocio"),
                    (3, "Persona Natural sin Negocio"),
                ],
                default=1,
            ),
        ),
    ]