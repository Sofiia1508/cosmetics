from django.shortcuts import render

def home_view(request):
    context = {
        'title': 'Головна сторінка Косметика',
        'welcome_message': 'Ласкаво просимо до світу краси та догляду!',
        'featured_products_title': 'Наші популярні товари:',
        'products': [
            {'name': 'Сироватка для обличчя', 'description': 'Інтенсивне зволоження та сяйво шкіри.'},
            {'name': 'Нічний крем', 'description': 'Відновлення та живлення під час сну.'},
            {'name': 'Шампунь для волосся', 'description': 'Зміцнення та блиск для всіх типів волосся.'},
        ]
    }
    return render(request, 'cosmetics/index.html', context)

def page1_view(request):
    context = {
        'title': 'Продукти для обличчя',
        'content': 'Тут буде інформація та список продуктів для догляду за обличчям.'
    }
    return render(request, 'cosmetics/view1.html', context)

def page2_view(request):
    context = {
        'title': 'Декор для дому',
        'content': 'Тут буде інформація про декор для дому та пов\'язані товари.'
    }
    return render(request, 'cosmetics/view2.html', context)

def page3_view(request):
    context = {
        'title': 'Косметика для волосся',
        'content': 'Тут буде інформація про засоби для догляду за волоссям.'
    }
    return render(request, 'cosmetics/view3.html', context)

def page4_view(request):
    context = {
        'title': 'Макіяж',
        'content': 'Тут буде інформація про декоративну косметику та макіяж.'
    }
    return render(request, 'cosmetics/view4.html', context)

def page5_view(request):
    context = {
        'title': 'Догляд за тілом',
        'content': 'Тут буде інформація про засоби для догляду за тілом.'
    }
    return render(request, 'cosmetics/view5.html', context)

# Функція для сторінки "Таксі" (якщо потрібна)
def taksi_view(request):
    context = {
        'title': 'Таксі',
        'content': 'Ця сторінка може містити інформацію про послуги таксі.'
    }