import json
from time import strftime
from django.http import HttpResponse
import datetime


def available_days(request):
    today = datetime.date.today()
    last_monday = today - datetime.timedelta(days=today.weekday())
    one_week = datetime.timedelta(days=7)
    next_monday = last_monday + one_week
    week = []
    week.append(next_monday.strftime('%Y-%m-%d'))
    days= 0
    while days < 5:
        next_day = next_monday + datetime.timedelta(days)
        week.append(next_day.strftime('%Y-%m-%d'))
        days += 1
    dates = week
    return HttpResponse(json.dumps(dates), content_type='application/json')
