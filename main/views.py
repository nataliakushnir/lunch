from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from main.forms import OrderForm
from main.models import Order, Dish


def index(request):
    return HttpResponseRedirect(reverse('order_history'))


def new(request):
    dishes = Dish.objects.all()
    user = request.user
    info = {}
    for dish in dishes:
        if dish.category.title in info:
            info[dish.category.title].append(dish)
        else:
            info[dish.category.title] = []
            info[dish.category.title].append(dish)

    order_form = OrderForm
    args = {}
    args.update(csrf(request))
    args['get_user'] = auth.get_user(request).username
    args['dishes'] = info
    args['form'] = order_form
    args['user'] = user
    return render_to_response('new.html', args)


def history(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/history/')
    return render_to_response('order_history.html', {'orders': Order.objects.filter(user_id=request.user.id),
                                                     'get_user': auth.get_user(request).username,
                                                     'user': request.user,
                                                     })


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/history/')
        else:
            args['login_error'] = 'User is not found'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/history/')


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username=new_user_form.cleaned_data['username'],
                                         password=new_user_form.cleaned_data['password2'])
            auth.login(request, new_user)
            return redirect('/history/')
        else:
            args['form'] = new_user_form
    return render_to_response('register.html', args)