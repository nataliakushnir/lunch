import json
from time import strftime
from django.http import HttpResponse
import datetime
from main.models import Order, Calendar


def available_days(request):
    week = []
    days = Calendar.objects.all()
    for day in days:
        if day.date > datetime.date.today():
            if day.date.strftime('%Y-%m-%d') not in week:
                week.append(day.date.strftime('%Y-%m-%d'))
    orders_days = []
    orders = Order.objects.all()
    for order in orders:
        orders_days.append(order.date.strftime('%Y-%m-%d'))
    dates = list(set(week) - set(orders_days))
    return HttpResponse(json.dumps(dates), content_type='application/json')