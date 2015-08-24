import json
from time import strftime
from django.http import HttpResponse
import datetime
from main.models import Order


def available_days(request):
    today = datetime.date.today()
    last_monday = today - datetime.timedelta(days=today.weekday())
    one_week = datetime.timedelta(days=7)
    next_monday = last_monday + one_week
    week = []
    days = 0
    while days < 5:
        next_day = next_monday + datetime.timedelta(days)
        if Order.objects.filter(date=next_day, ).exists():
            pass
        else:
            week.append(next_day.strftime('%Y-%m-%d'))
        days += 1
    dates = week
    return HttpResponse(json.dumps(dates), content_type='application/json')
