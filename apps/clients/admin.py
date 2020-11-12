from django.contrib import admin
from config.apps.clients.models import Client
from config.apps.clients.models import Contact
from config.apps.clients.models import Bankaccount


admin.site.register(Client)
admin.site.register(Contact)
admin.site.register(Bankaccount)
