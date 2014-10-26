from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
  url(r'^$', views.root_page),
  url(r'^(?P<pk>[0-9]+)/edit/$', views.edit_link, name='edit_link')
)