from django.contrib import admin
from config.apps.warehouse.models import Category
from config.apps.warehouse.models import Tags
from config.apps.warehouse.models import Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Product)
