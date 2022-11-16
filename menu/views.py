from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    return render(request, 'menu/home.html')


def sushi(request):
    normal_sushi_list = Roll.objects.filter(special=False).order_by('name')
    special_sushi_list = Roll.objects.filter(special=True).order_by('name')
    sushi_sashimi_list = SushiSashimi.objects.all().order_by('name')
    context = {
        'normal_sushi_list': normal_sushi_list,
        'special_sushi_list': special_sushi_list,
        'sushi_sashimi_list': sushi_sashimi_list,
    }
    return render(request, 'menu/sushi.html', context)


def appetizer(request):
    appetizer_sushi_list = Appetizer.objects.filter(kitchen=False).order_by('name')
    appetizer_kitchen_list = Appetizer.objects.filter(kitchen=True).order_by('name')
    context = {
        'appetizer_sushi_list': appetizer_sushi_list,
        'appetizer_kitchen_list': appetizer_kitchen_list,
    }
    return render(request, 'menu/aptzr.html', context)


def hibachi(request):
    hibachi_lunch_list = HibachiLunch.objects.all().order_by('price')
    context = {
        'hibachi_list': hibachi_lunch_list
    }
    return render(request, 'menu/hibachi.html', context)


def kitchen(request):
    kitchen_dinner_list = KitchenDinner.objects.all().order_by('price')
    context = {
        'kitchen_list': kitchen_dinner_list
    }
    return render(request, 'menu/kitchen.html', context)


def soup_salad(request):
    soup_list = Soup.objects.all().order_by('price')
    salad_list = Salad.objects.all().order_by('price')
    context = {
        'soup_list': soup_list,
        'salad_list': salad_list,
    }
    return render(request, 'menu/soup_salad.html', context)


def noodle_rice(request):
    return render(request, 'menu/noodle_rice.html')


def sushi_dinner(request):
    return render(request, 'menu/sushi_dinner.html')


def roll_combo(request):
    return render(request, 'menu/roll_combo.html')


def dessert(request):
    return render(request, 'menu/dessert.html')

