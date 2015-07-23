from django.template import Context
from django.shortcuts import render_to_response
from django.template.loader import get_template


def add_order(request):
    view = 'yes'
    return render_to_response('main.html', {'add': view})