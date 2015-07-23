from django.conf.urls import include, url

urlpatterns = [
    url(r'^add/', 'main.views.add_order'),
]

