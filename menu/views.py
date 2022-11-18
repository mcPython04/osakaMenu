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
    lunch_list = HibachiLunch.objects.all().order_by('price')
    dinner_list = HibachiDinner.objects.all().order_by('price')
    kid_list = HibachiKid.objects.all().order_by('price')
    context = {
        'lunch_list': lunch_list,
        'dinner_list': dinner_list,
        'kid_list': kid_list,
    }
    return render(request, 'menu/hibachi.html', context)


def kitchen(request):
    box_list = BentoBox.objects.all().order_by('price')
    dinner_list = KitchenDinner.objects.all().order_by('price')
    context = {
        'dinner_list': dinner_list,
        'box_list': box_list,
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
    noodle_list = Noodle.objects.all().order_by('price')
    rice_list = FriedRice.objects.all().order_by('price')
    context = {
        'noodle_list': noodle_list,
        'rice_list': rice_list,
    }
    return render(request, 'menu/noodle_rice.html', context)


def sushi_dinner(request):
    dinner_list = SushiDinner.objects.all().order_by('price')
    context = {
        'dinner_list': dinner_list,
    }
    return render(request, 'menu/sushi_dinner.html', context)


def roll_combo(request):
    roll_list = Roll.objects.filter(combo=True).order_by('name')
    context = {
        'roll_list': roll_list
    }
    return render(request, 'menu/roll_combo.html', context)


def dessert(request):
    dessert_list = Dessert.objects.all().order_by('price')
    context = {
        'dessert_list': dessert_list,
    }
    return render(request, 'menu/dessert.html', context)


def menu(request):
    return render(request, 'menu/menu_nav.html')
