import datetime
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import redirect, render
from django.utils.decorators import decorator_from_middleware_with_args
from .forms import OrderForm, LoginUserForm, RegistrationForm
from main.messages import SendMessage
from .models import Order, Dish, Calendar, Calculate, Category
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
                    count = request.POST['count_' + str(item_id)]
                    Calculate.objects.create(order=order, dish=Dish.objects.get(id=item_id), count=count)
                    args['alert_success'] = "Your order created successfully!"
                    OrderForm.dates.remove(str(order.date))
                else:
                    args['custom_alert'] = "Any item not selected"
    new_order = OrderForm(request.GET)
    info = []
    if request.GET:
        date = request.GET.get('date')
        dishes_for_date = Calendar.objects.filter(date=date)
        if date in OrderForm.dates:
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
    args['user'] = auth.get_user(request)
    # TODO change SMTP server
    # try:
    #     if args['alert_success'] is not None:
    #         SendMessage.order_success(request)
    # except:
    #     pass
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
    info = {}
    for order in orders:
        order_info = []
        for calculate in Calculate.objects.filter(order=order):
            order_info.append(calculate)
            info[order.id] = order_info
    return render(request, 'order_history.html', {'orders': orders,
                                                  'sort': sort,
                                                  'dishes': info,
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

            # TODO change SMTP server
            # SendMessage.register_success(request)
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


def private(request):
    args = {}
    period = request.GET.get('statistic')

    # get dates for this week

    today = datetime.date.today()
    last_monday = today - datetime.timedelta(days=today.weekday())
    one_week = datetime.timedelta(days=7)
    end_of_week = last_monday + one_week - datetime.timedelta(days=1)
    start_period = last_monday
    end_period = end_of_week
    d = start_period
    week = []
    delta = datetime.timedelta(days=1)
    while d <= end_period:
        week.append(d.strftime("%Y-%m-%d"))
        d+=delta

    # get custom dates

    start = request.POST.get('date_from')
    end = request.POST.get('date_to')


    category_list = []
    for dish in Dish.objects.all():
        if dish.category not in category_list:
            category_list.append(dish.category)
    count_of_dishes_in_categories = {}
    for category in Category.objects.all():
        s = 0
        t = 0
        for calculate in Calculate.objects.all():
            if period == 'week':
                args['start'] = start_period
                args['end'] = end_period
                if calculate.dish.category == category:
                    d = start_period
                    week = []
                    delta = datetime.timedelta(days=1)
                    while d <= end_period:
                        week.append(d.strftime("%Y-%m-%d"))
                        d+=delta
                    if calculate.date().strftime("%Y-%m-%d") in week:
                        s += calculate.count
                        t += calculate.total()
                        count_of_dishes_in_categories[category] = [s, t]
            elif period == 'month':
                if calculate.date().month == datetime.date.today().month:
                    if calculate.dish.category == category:
                        s += calculate.count
                        t += calculate.total()
                        args['month'] = today.strftime('%B')
                    count_of_dishes_in_categories[category] = [s, t]
            elif period == 'year':
                if calculate.date().year == datetime.date.today().year:
                    if calculate.dish.category == category:
                        s += calculate.count
                        t += calculate.total()
                        args['year'] = today.strftime('%Y')
                    count_of_dishes_in_categories[category] = [s, t]
            elif period == 'custom':
                args['custom_date'] = 1
                if request.POST:
                    try:
                        start_period = datetime.datetime.strptime(datetime.datetime.strptime(start, '%m/%d/%Y').strftime('%Y-%d-%m'), '%Y-%d-%m').date()
                        end_period = datetime.datetime.strptime(datetime.datetime.strptime(end, '%m/%d/%Y').strftime('%Y-%d-%m'), '%Y-%d-%m').date()
                        if start_period > end_period:
                            args['dates_alert'] = "Please insert correct date range"
                        if start_period and end_period:
                            args['start'] = start_period
                            args['end'] = end_period
                            if calculate.dish.category == category:
                                d = start_period
                                custom_period = []
                                delta = datetime.timedelta(days=1)
                                while d <= end_period:
                                    custom_period.append(d.strftime("%Y-%m-%d"))
                                    d+=delta
                                if calculate.date().strftime("%Y-%m-%d") in custom_period:
                                    s += calculate.count
                                    t += calculate.total()
                                    count_of_dishes_in_categories[category] = [s, t]
                        else:
                            args['dates_alert'] = "Please insert correct date range"
                    except:
                        args['dates_alert'] = "Please insert correct date range"
            else:
                if calculate.dish.category == category:
                    s += calculate.count
                    t += calculate.total()
                    args['all'] = 'all times'
                count_of_dishes_in_categories[category] = [s, t]
    args['counts'] = count_of_dishes_in_categories
    args['categories'] = category_list

    return render(request, 'personal account.html', args)
