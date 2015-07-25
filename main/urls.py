from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^$', 'main.views.index', name='index'),
    url(r'^history/', 'main.views.history', name='order_history'),
    url(r'^new/', 'main.views.new', name='new_order'),
]
