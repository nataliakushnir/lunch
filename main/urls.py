from django.conf.urls import url
from django.shortcuts import render_to_response
from django.template import RequestContext

urlpatterns = [
    url(r'^$', 'main.views.index', name='index'),
    url(r'^home/history/', 'main.views.history', name='order_history'),
    url(r'^home/new/', 'main.views.new', name='new_order'),
    url(r'^login/', 'main.views.login', name='login'),
    url(r'^logout/', 'main.views.logout', name='logout'),
    url(r'^register/', 'main.views.register', name='register'),
    url(r'^home/private/', 'main.views.private', name='private'),

    # ajax methods
    url(r'^ajax/available-days', 'main.ajax.available_days', name='available_days'),
]


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
