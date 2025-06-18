# DjangoProject1/cosmetics/views.py

from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def home_view(request):
    """
    Відображає головну сторінку з усіма доступними продуктами
    та категоріями для навігації.
    """
    products = Product.objects.filter(available=True) # Отримуємо всі доступні продукти
    categories = Category.objects.all() # Отримуємо всі категорії для навігації

    context = {
        'title': 'Головна сторінка Косметика',
        'welcome_message': 'Ласкаво просимо до світу краси та догляду!',
        'products': products,
        'categories': categories, # Передаємо категорії до шаблону для відображення в навігації
    }
    # ПЕРЕКОНАЙТЕСЯ, ЩО ШЛЯХ ДО ШАБЛОНУ КОРЕКТНИЙ: cosmetics/index.html
    return render(request, 'cosmetics/index.html', context)

def product_list(request, category_slug=None):
    """
    Відображає список продуктів, відфільтрованих за категорією,
    або всі продукти, якщо категорія не вказана.
    """
    category = None
    categories = Category.objects.all() # Отримуємо всі категорії для навігації
    products = Product.objects.filter(available=True)

    if category_slug:
        # Отримуємо об'єкт категорії або повертаємо 404, якщо не знайдено
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category) # Фільтруємо продукти за обраною категорією

    context = {
        'category': category,
        'categories': categories, # Передаємо категорії для навігації
        'products': products
    }
    # ПЕРЕКОНАЙТЕСЯ, ЩО ШЛЯХ ДО ШАБЛОНУ КОРЕКТНИЙ: cosmetics/product/list.html
    return render(request, 'cosmetics/product/list.html', context)

def product_detail(request, id, slug):
    """
    Відображає детальну інформацію про конкретний продукт.
    """
    # Отримуємо продукт за ID та slug або повертаємо 404
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    categories = Category.objects.all() # Отримуємо всі категорії для навігації

    context = {
        'product': product,
        'categories': categories, # Передаємо категорії для навігації
    }
    # ПЕРЕКОНАЙТЕСЯ, ЩО ШЛЯХ ДО ШАБЛОНУ КОРЕКТНИЙ: cosmetics/product/detail.html
    return render(request, 'cosmetics/product/detail.html', context)

# --- Старі статичні в'юшки, які викликають помилки NoReverseMatch, ВИДАЛІТЬ ЇХ! ---
# def page1_view(request):
#     context = {
#         'title': 'Продукти для обличчя (Статична)',
#         'content': 'Це статична сторінка для продуктів для обличчя.'
#     }
#     return render(request, 'cosmetics/view1.html', context)

# def page2_view(request):
#     context = {
#         'title': 'Декор для дому (Статична)',
#         'content': 'Це статична сторінка для декору для дому.'
#     }
#     return render(request, 'cosmetics/view2.html', context)

# def page3_view(request):
#     context = {
#         'title': 'Косметика для волосся (Статична)',
#         'content': 'Це статична сторінка для косметики для волосся.'
#     }
#     return render(request, 'cosmetics/view3.html', context)

# def page4_view(request):
#     context = {
#         'title': 'Макіяж (Статична)',
#         'content': 'Це статична сторінка для макіяжу.'
#     }
#     return render(request, 'cosmetics/view4.html', context)

# def page5_view(request):
#     context = {
#         'title': 'Догляд за тілом (Статична)',
#         'content': 'Це статична сторінка для догляду за тілом.'
#     }
#     return render(request, 'cosmetics/view5.html', context)

# def all_products_view(request):
#     context = {
#         'title': 'Всі Продукти (Статична)',
#         'content': 'Це статична сторінка для всіх продуктів.'
#     }
#     return render(request, 'cosmetics/view6.html', context)