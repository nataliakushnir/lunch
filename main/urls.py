from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^$', 'main.views.index', name='index'),
    url(r'^home/history/', 'main.views.history', name='order_history'),
    url(r'^home/new/', 'main.views.new', name='new_order'),
    url(r'^login/', 'main.views.login', name='sign_in'),
    url(r'^logout/', 'main.views.logout', name='logout'),
    url(r'^register/', 'main.views.register', name='register'),
    url(r'^home/', 'main.views.home', name='home'),
]