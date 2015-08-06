from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect, render
from django.utils.decorators import decorator_from_middleware_with_args
from .forms import OrderForm, LoginUserForm, RegisterForm
from .models import Order, Dish
from middlewares import CustomAuthMiddleware


only_auth = decorator_from_middleware_with_args(CustomAuthMiddleware)

def index(request):
    return redirect('home')

@only_auth()
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


@only_auth()
def history(request):
    if request.POST:
        new_order_form = OrderForm(request.POST)
        if new_order_form.is_valid():
            new_order_form.save()
            return redirect('order_history')
        else:
            return redirect('new_order')
    return render_to_response('order_history.html', {'orders': Order.objects.all(),
                                                     'username': request.user.username,})


def login(request):
    args = {}
    args.update(csrf(request))

    if request.method == 'POST':
        login_form = LoginUserForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                args['custom_error'] = 'Login and/or password are wrong'
        args['form'] = login_form
        return render(request, 'login.html', args)
    else:
        login_form = LoginUserForm()
        args['login_form'] = login_form
    return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('home')


def register(request):
    args = {}
    args.update(csrf(request))
    args['user_register'] = RegisterForm()
    if request.POST:
        new_user = UserCreationForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            new_user = auth.authenticate(username=new_user.cleaned_data['username'],
                                         password=new_user.cleaned_data['password2'],
                                         )
            auth.login(request, new_user)
            return redirect('new_order')
        else:
            args['user_register'] = new_user
    return render_to_response('register.html', args)


def home(request):
    if request.user.is_authenticated():
        return render_to_response('layouts/main_logged_in.html')
    else:
        return render_to_response('layouts/main_not_logged.html')
