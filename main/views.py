from django.contrib import auth
from django.core.context_processors import csrf
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import get_template
from django.utils.decorators import decorator_from_middleware_with_args
from .forms import OrderForm, LoginUserForm, RegistrationForm
from .models import Order, Dish
from middlewares import CustomAuthMiddleware

only_auth = decorator_from_middleware_with_args(CustomAuthMiddleware)


def index(request):
    if request.user.is_authenticated():
        return redirect('home')
    else:
        return redirect('login')


@only_auth()
def new(request):
    args = {}
    if request.POST:
        order = Order()
        order.user = request.user
        order.date = request.POST.get("date", )
        try:
            order.save()
            for key in request.POST:
                if "dish_" in key:
                    item_id = int(key[5:])
                    order.items.add(Dish.objects.get(id=item_id))
                    args['alert_success'] = "Your order created successfully!"
                else:
                    args['custom_alert'] = "Any item not selected"
        except ValidationError:
            args['custom_alert'] = "Please enter correct date"
    new_order = OrderForm
    dishes = Dish.objects.all()
    info = {}
    for dish in dishes:
        if dish.category.title in info:
            info[dish.category.title].append(dish)
        else:
            info[dish.category.title] = []
            info[dish.category.title].append(dish)
    args.update(csrf(request))
    args['new_order'] = new_order
    args['dishes'] = info
    args['user'] = auth.get_user(request)
    try:
        if args['alert_success'] is not None:
            html_order = get_template('email_order.html', )
            order_html = Context({'order': Order.objects.last(),
                                  'username': request.user.username})
            html_content = html_order.render(order_html)
            subject = 'Order'
            from_email = 'natalia.l.kushnir@gmail.com'
            to = auth.get_user(request).email
            msg = EmailMultiAlternatives(subject, '', from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
    except:
        pass
    return render(request, 'new.html', args)


@only_auth()
def history(request):
    return render(request, 'order_history.html', {'orders': Order.objects.filter(user_id=request.user.id),
                                                  'username': request.user.username, })


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
    return redirect('home')


def home(request):
    if request.user.is_authenticated():
        return redirect('new_order')
    else:
        return redirect('login')
