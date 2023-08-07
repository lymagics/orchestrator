from django.urls import path

from ping.views import ping

urlpatterns = [
    path('', ping, name='ping'),
]

app_name = 'ping'
