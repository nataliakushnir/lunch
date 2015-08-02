from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from main.forms import OrderForm
from main.models import Order, Dish


def index(request):
    if request.user.is_authenticated():
        return redirect('home')
    else:
        return render_to_response('index.html')


def new(request):
    new_order = OrderForm
    dishes = Dish.objects.all()
    info = {}
    for dish in dishes:
        if dish.category.title in info:
            info[dish.category.title].append(dish)
        else:
            info[dish.category.title] = []
            info[dish.category.title].append(dish)
    args = {}
    args.update(csrf(request))
    args['new_order'] = new_order
    args['dishes'] = info
    args['username'] = auth.get_user(request).username
    return render_to_response('new.html', args)


def history(request):
    user = request.user
    if request.POST:
        new_order_form = OrderForm(request.POST)
        if new_order_form.is_valid():
            new_order_form.save()
            return redirect('order_history')
        else:
            return redirect('new_order')
    return render_to_response('order_history.html', {'orders': Order.objects.filter(user_id=user.id),
                              'username': request.user.username})

def login(request):
    new_user = AuthenticationForm
    args = {}
    args.update(csrf(request))
    args['new_user'] = new_user
    args['username'] = auth.get_user(request).username
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            args['login_error'] = 'User is not found'
            return redirect('login')
    return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    args = {}
    args.update(csrf(request))
    args['user_register'] = UserCreationForm()
    if request.POST:
        new_user = UserCreationForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            new_user = auth.authenticate(username=new_user.cleaned_data['username'], password=new_user.cleaned_data['password2'])
            auth.login(request, new_user)
            return redirect('new_order')
        else:
            args['user_register'] = new_user
    return render_to_response('register.html', args)


def home(request):
    if request.user.is_authenticated():
        return render_to_response('home.html', {'username': auth.get_user(request).username})
    else:
        return redirect('login')
