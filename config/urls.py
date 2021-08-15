from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('account/', include('account_auth.urls')),
    path('profile/', include('accounts.urls')),
    path('templates/', include('template_manager.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

