# cosmetics/urls.py

from django.urls import path
from . import views

# ОБОВ'ЯЗКОВО: Це визначає простір імен для URL-маршрутів цієї програми.
# Це дозволить використовувати {% url 'cosmetics:home' %} тощо.
app_name = 'cosmetics'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('view1/', views.page1_view, name='page1'),
    path('view2/', views.page2_view, name='page2'),
    path('view3/', views.page3_view, name='page3'),
    path('view4/', views.page4_view, name='page4'),
    path('view5/', views.page5_view, name='page5'),
]