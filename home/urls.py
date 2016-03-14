__author__ = 'ali'

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^add/$', views.add_post, name='add_post'),
                       url(r'^delete_post/$', views.del_post, name='delete_post'),
                       url(r'^tag/(?P<tag_name>[^/]+)/$', views.tag_page, name='tag_page'),
                       )
