from django.conf.urls import patterns, url
from wifipulling import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^$',views.index_2, name='index_2'),
    url(r'^$',views.aggregate, name='aggregate'))