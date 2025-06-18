# DjangoProject1/cosmetics/urls.py

from django.urls import path
from . import views

app_name = 'cosmetics' # Важливо для використання в {% url 'cosmetics:...' %}

urlpatterns = [
    # Головна сторінка, яка відображає всі продукти
    path('', views.home_view, name='home'),

    # URL-адреса для списку продуктів за конкретною категорією
    # <slug:category_slug> - це динамічний сегмент URL, який відповідає slug категорії
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),

    # URL-адреса для детальної сторінки продукту
    # <int:id> - це ID продукту, <slug:slug> - це slug продукту
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

    # --- Старі статичні URL-адреси, ВИДАЛІТЬ ЇХ! ---
    # Ці URL-адреси викликають помилку NoReverseMatch, оскільки ви видалили відповідні view-функції.
    # path('view1/', views.page1_view, name='page1'),
    # path('view2/', views.page2_view, name='page2'),
    # path('view3/', views.page3_view, name='page3'),
    # path('view4/', views.page4_view, name='page4'),
    # path('view5/', views.page5_view, name='page5'),
    # path('all-products/', views.all_products_view, name='all_products'),
]