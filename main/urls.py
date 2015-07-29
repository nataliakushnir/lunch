from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^$', 'main.views.index', name='index'),
    url(r'^history/', 'main.views.history', name='order_history'),
    url(r'^new/', 'main.views.new', name='new_order'),
    url(r'^auth/login/', "main.views.login",),
    url(r'^auth/logout/', "main.views.logout",),
    url(r'^auth/register/', "main.views.register",)
]
