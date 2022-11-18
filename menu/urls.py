from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('sushi/', views.sushi, name='sushi'),
    path('appetizer/', views.appetizer, name='appetizer'),
    path('hibachi/', views.hibachi, name='hibachi'),
    path('kitchen/', views.kitchen, name='kitchen'),
    path('noodle_rice/', views.noodle_rice, name='noodle_rice'),
    path('roll_combo/', views.roll_combo, name='roll_combo'),
    path('soup_salad/', views.soup_salad, name='soup_salad'),
    path('sushi_dinner/', views.sushi_dinner, name='sushi_dinner'),
    path('dessert/', views.dessert, name='dessert'),
]
