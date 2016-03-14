from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from home.PostSitemap import PostSitemap


sitemaps = {
    'posts': PostSitemap(),
}



urlpatterns = patterns('',

                       url(r'^$', 'home.views.index', name='home'),
                       url(r'^home/', include('home.urls', namespace='home')),
                       url(r'^search/', include('haystack.urls')),

                       url(r'^rate_up/$', 'home.views.rate_up', name='rate_up'),
                       # url(r'^rate_up/(?P<post_id>\d+)/$', 'home.views.rate_up', name='rate_up'),
                       url(r'^rate_down/$', 'home.views.rate_down', name='rate_down'),
                       # url(r'^rate_down/(?P<post_id>\d+)/$', 'home.views.rate_down', name='rate_down'),

                       url(r'^accounts/', include('accounts.urls', namespace='accounts')),
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^users/$', 'home.views.users_list', name='user_list'),
                       url(r'^user/(?P<username>[.\w]+)/$', 'home.views.user_page', name='user_page'),
                       url(r'^followings/$', 'home.views.follows_list', name='followings'),
                       url(r'^followers/$', 'home.views.followed_by_list', name='followers'),
                       url(r'^public/$', 'home.views.public_posts', name='public'),

                       url(r'^follow/(?P<username>[.\w]+)/$', 'home.views.follow', name='follow'),
                       url(r'^unfollow/(?P<username>[.\w]+)/$', 'home.views.unfollow', name='unfollow'),
                       url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
                           name='django.contrib.sitemaps.views.sitemap')
                       )
