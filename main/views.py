from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from main.models import Category, Dish, Order


def index(request):
    return HttpResponseRedirect(reverse('order_history'))


def new(request):
    dishes = Dish.objects.all()
    info = {}

    for dish in dishes:

        if dish.category.title in info:
            info[dish.category.title].append(dish)
        else:
            info[dish.category.title] = []
            info[dish.category.title].append(dish)

    return render_to_response('new.html', {'dishes': info})


def history(request):
    return render_to_response('order_history.html', {'orders': Order.objects.filter(user_id=request.user.id)})
