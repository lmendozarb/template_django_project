from django.contrib import admin
from ecommerce.apps.clients.models import Client
from ecommerce.apps.clients.models import Contact
from ecommerce.apps.clients.models import Bankaccount

admin.site.register(Client)
admin.site.register(Contact)
admin.site.register(Bankaccount)
