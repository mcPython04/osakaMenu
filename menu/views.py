from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    return render(request, 'menu/home.html')


def sushi(request):
    normal_sushi_list = Sushi.objects.filter(special=False).order_by('name')
    special_sushi_list = Sushi.objects.filter(special=True).order_by('name')
    context = {
        'normal_sushi_list': normal_sushi_list,
        'special_sushi_list': special_sushi_list,
    }
    return render(request, 'menu/sushi.html', context)


def appetizer(request):
    appetizer_list = Appetizers.objects.all().order_by('name')
    context = {
        'appetizer_list': appetizer_list
    }
    return render(request, 'menu/aptzr.html', context)


def hibachi(request):
    hibachi_list = Hibachi.objects.all().order_by('price')
    context = {
        'hibachi_list': hibachi_list
    }
    return render(request, 'menu/hibachi.html', context)


def kitchen(request):
    kitchen_list = Kitchen.objects.all().order_by('price')
    context = {
        'kitchen_list': kitchen_list
    }
    return render(request, 'menu/kitchen.html', context)

