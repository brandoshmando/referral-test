from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
  url(r'^$', views.root_page, name='root_page'),
  url(r'^(?P<pk>[0-9]+)/edit/$', views.edit_link, name='edit_link'),
  url(r'^(?P<pk>[0-9]+)/delete/$', views.delete_link, name='delete_link'),
  url(r'^landing/$', views.landing_page, name='landing_page'),
  url(r'^links/$', views.active_links, name='active_links')
)