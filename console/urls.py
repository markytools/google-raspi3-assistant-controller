from django.conf.urls import url

from . import views

app_name = 'console'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^data/$', views.data, name='data'),
]
