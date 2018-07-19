from django.conf.urls import url

from . import views

app_name = 'media'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^musiclib/', views.musiclib, name='musiclib'),
    url(r'^playlist/', views.playlist, name='playlist'),
]
