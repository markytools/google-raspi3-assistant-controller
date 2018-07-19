from django.conf.urls import url

from . import views

app_name = 'linphoneapp'
urlpatterns = [
    url(r'^$', views.linphoneapp, name='linphoneapp'),
]
