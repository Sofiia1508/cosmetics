# cosmetics/urls.py

from django.urls import path
from . import views # <--- ВАЖЛИВО: Імпортуємо views з поточної директорії

urlpatterns = [
    # Головна сторінка нашого додатку
    path('', views.index, name='index'),

    # Шляхи до ваших 5 додаткових сторінок
    path('view1/', views.view1, name='view1'),
    path('view2/', views.view2, name='view2'),
    path('view3/', views.view3, name='view3'),
    path('view4/', views.view4, name='view4'),
    path('view5/', views.view5, name='view5'),
]