# DjangoProject1/DjangoProject1/urls.py

from django.contrib import admin
from django.urls import path, include

# Імпорти для обслуговування медіафайлів у режимі розробки
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # URL-адреса для адмін-панелі Django
    path('', include('cosmetics.urls')), # Включаємо URL-адреси з нашого додатку 'cosmetics'
]

# Обслуговування медіафайлів тільки в режимі DEBUG (для розробки)
# У виробничому середовищі це має оброблятися веб-сервером (nginx, apache)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)