from django.template import Context
from django.shortcuts import render_to_response
from django.template.loader import get_template
from main.models import Category, Dish

def category(request):
    d = Category.objects.get(id=2)
    return render_to_response('main.html', {'categories': Category.objects.all(), 'dishes': Dish.objects.filter(category_id=d)})




