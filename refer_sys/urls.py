from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
  url(r'^$', views.root_page)
  # url(r'^POST?$', views.create_link)
)