from django.conf.urls import patterns, url
from wifipulling import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'aggregate$',views.aggregate,name='aggregate')