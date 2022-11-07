from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sushi/', views.sushi, name='sushi'),
    path('appetizers/', views.appetizer, name='appetizer')
]
