# DjangoProject1/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Включаємо URL-адреси з нашого додатку 'cosmetics'
    # Всі запити до кореня сайту ('') будуть оброблятися 'cosmetics.urls'
    path('', include('cosmetics.urls')), # <--- ЦЕЙ РЯДОК ВИПРАВЛЯЄ ПОМИЛКУ ImportError
]