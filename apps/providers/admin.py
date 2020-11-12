from django.contrib import admin
from config.apps.providers.models import Providers
from config.apps.providers.models import ProvidersContact

admin.site.register(Providers)
admin.site.register(ProvidersContact)
