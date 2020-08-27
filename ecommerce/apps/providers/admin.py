from django.contrib import admin
from ecommerce.apps.providers.models import Providers
from ecommerce.apps.providers.models import ProvidersContact

admin.site.register(Providers)
admin.site.register(ProvidersContact)
