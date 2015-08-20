import json
from django.http import HttpResponse


def available_days(request):
    dates = ["2015-08-24", "2015-08-25", "2015-08-26", "2015-08-27", "2015-08-28"]
    return HttpResponse(json.dumps(dates), content_type='application/json')
