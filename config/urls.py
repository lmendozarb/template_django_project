from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
