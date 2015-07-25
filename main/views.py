from django.shortcuts import render_to_response
from main.models import Category, Dish


def category(request):
    dishes = Dish.objects.all()
    return render_to_response('main.html', {'categories': Category.objects.all(), 'dishes': dishes})
