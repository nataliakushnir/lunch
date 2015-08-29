from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import redirect, render
from django.utils.decorators import decorator_from_middleware_with_args
from .forms import OrderForm, LoginUserForm, RegistrationForm
from main.messages import SendMessage
from .models import Order, Dish, Calendar, Calculate
from middlewares import CustomAuthMiddleware
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


only_auth = decorator_from_middleware_with_args(CustomAuthMiddleware)


def index(request):
    if request.user.is_authenticated():
        return redirect('new_order')
    else:
        return redirect('login')


@only_auth()
def new(request):
    args = {}
    if request.POST:
        order = Order()
        order.user = request.user
        order.date = request.POST.get("date", )
        if order.date in OrderForm.dates:
            for key in request.POST:
                if "dish_" in key:
                    order.save(request.GET)
                    item_id = int(key[5:])

                    Calculate.objects.create(order=order, dish=Dish.objects.get(id=item_id), count=count)
                    args['alert_success'] = "Your order created successfully!"
                else:
                    args['custom_alert'] = "Any item not selected"
    new_order = OrderForm(request.GET)
    date = request.GET.get('date')
    info = []
    if request.GET:
        if date in OrderForm.dates:
            dishes_for_date = Calendar.objects.filter(date=date)
            for dish in dishes_for_date:
                info.append(dish.dish)
        else:
            args['available_dates_alert'] = "Please enter correct date"
    category_info = {}
    for dish in info:
        dish_info = Dish.objects.filter(name=dish)
        for dish in dish_info:
            if dish.category.title not in dish_info:
                category_info.setdefault(dish.category, [])
                category_info.setdefault(dish.category, []).append(dish)
    args.update(csrf(request))
    args['new_order'] = new_order
    args['categories'] = category_info
    args['dishes'] = category_info.values()
    args['user'] = auth.get_user(request)
    try:
        if args['alert_success'] is not None:
            SendMessage.order_success(request)
    except:
        pass
    return render(request, 'new.html', args)


@only_auth()
def history(request):
    sort = request.GET.get('sort')
    if sort == 'summ':
        user_orders = sorted(Order.objects.filter(user_id=request.user.id), key=lambda t: t.total())
    else:
        user_orders = Order.objects.filter(user_id=request.user.id).order_by('-date')
    paginator = Paginator(user_orders, 5)

    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    return render(request, 'order_history.html', {'orders': orders,
                                                  'sort': sort,
                                                  'username': request.user.username, })


def login(request):
    if request.user.is_authenticated():
        return redirect('index')

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
                return redirect('new_order')
            else:
                args['custom_error'] = 'Login and/or password are wrong'
        args['login_form'] = login_form
        return render(request, 'login.html', args)
    else:
        login_form = LoginUserForm()
        args['login_form'] = login_form
    return render(request, 'login.html', args)


def register(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            new_user = auth.authenticate(username=register_form.cleaned_data['username'],
                                         password=register_form.cleaned_data['password2'], )
            auth.login(request, new_user)
            SendMessage.register_success(request)
            return redirect('new_order')
        else:
            args['custom_error'] = register_form
        args['register_form'] = register_form
        return render(request, 'register.html', args)
    else:
        register_form = RegistrationForm()
        args['register_form'] = register_form
    return render(request, 'register.html', args)


def logout(request):
    auth.logout(request)
    return redirect('index')
