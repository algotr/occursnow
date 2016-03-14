__author__ = 'ali'

from django.conf.urls import patterns, url


urlpatterns = patterns('accounts.views',
                       url(r'^login/$', 'login', name='login'),
                       url(r'^logout/$', 'logout', name='logout'),
                       url(r'^register/$', 'register', name='register'),
                       url(r'^profile/$', 'profile', name='profile'),
                       )
