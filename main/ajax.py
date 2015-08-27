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
            week.append(day.date.strftime('%Y-%m-%d'))
    dates = week
    return HttpResponse(json.dumps(dates), content_type='application/json')
