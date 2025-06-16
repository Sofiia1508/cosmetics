from django.shortcuts import render
from django.http import HttpResponse # Додайте, якщо використовуєте HttpResponse

def index(request):
    """
    Представленння для відображення головної сторінки.
    """
    context = {
        'page_title': 'Головна Сторінка',
        'welcome_message': 'Ласкаво просимо до нашого магазину косметики!',
        'featured_product': 'Новий крем для обличчя з гіалуроновою кислотою!',
        'num_products': 125,
        'num_categories': 15,
    }
    return render(request, 'cosmetics/index.html', context)

# Функції для ваших 5 view-ів
def view1(request):
    context = {'title': 'Сторінка 1'}
    return render(request, 'cosmetics/view1.html', context)

def view2(request):
    context = {'title': 'Сторінка 2'}
    return render(request, 'cosmetics/view2.html', context)

def view3(request):
    context = {'title': 'Сторінка 3'}
    return render(request, 'cosmetics/view3.html', context)

def view4(request):
    context = {'title': 'Сторінка 4'}
    return render(request, 'cosmetics/view4.html', context)

def view5(request):
    context = {'title': 'Сторінка 5'}
    return render(request, 'cosmetics/view5.html', context)