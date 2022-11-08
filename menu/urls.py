from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sushi/', views.sushi, name='sushi'),
    path('appetizers/', views.appetizer, name='appetizer'),
    path('hibachi/', views.hibachi, name='hibachi'),
    path('kitchen/', views.kitchen, name='kitchen'),
]
