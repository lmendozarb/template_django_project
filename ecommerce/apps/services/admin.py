from django.contrib import admin
from ecommerce.apps.services.models import Shipping
from ecommerce.apps.services.models import ShippingConfigure

# Register your models here.

admin.site.register(Shipping)
admin.site.register(ShippingConfigure)
