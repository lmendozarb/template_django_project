from django.db import models


class Category(models.Model):
    name = models.CharField("Nombre", max_length=255)
    slug = models.SlugField("Slug", max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="Category/", default="")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return f"{self.name}"


class Tags(models.Model):
    name = models.CharField("Nombre", max_length=255)
    slug = models.SlugField("Slug", max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    product_name = models.CharField("Nombre del Producto", max_length=255)
    sku = models.CharField("SKU", max_length=255)
    short_description = models.CharField("Descripción Corta", max_length=50)
    long_description = models.CharField("Descripción", max_length=255)
    regular_price = models.DecimalField(
        "Precio Regular", max_digits=10, decimal_places=2
    )
    sales_prices = models.DecimalField(
        "Precio de Venta", max_digits=10, decimal_places=2
    )
    sold_individually = models.CharField("Venta Individual", max_length=255)
    weight = models.DecimalField("Peso", max_digits=10, decimal_places=2)
    lenght = models.DecimalField("Largo", max_digits=10, decimal_places=2)
    width = models.DecimalField("Ancho", max_digits=10, decimal_places=2)
    height = models.DecimalField("Alto", max_digits=10, decimal_places=2)
    purchase_note = models.CharField("Nota de Compra", max_length=255)
    category = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tags)
    product_image1 = models.ImageField(upload_to="Product/")
    product_image2 = models.ImageField(upload_to="Product/")
    product_image3 = models.ImageField(upload_to="Product/")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.product_name}"
