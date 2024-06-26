from django.contrib import admin
from django.urls import path, include

# DUAS NOVAS IMPORTAÇÕES
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bikes.urls')),
    path('registration/', include('registration.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


