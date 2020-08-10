from django.contrib import admin
from ecommerce.apps.clients.models import Client
from ecommerce.apps.clients.models import Contact

admin.site.register(Client)
admin.site.register(Contact)
