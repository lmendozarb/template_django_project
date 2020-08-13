from django.contrib import admin
from ecommerce.apps.warehouse.models import Category
from ecommerce.apps.warehouse.models import Tags
from ecommerce.apps.warehouse.models import Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Product)
