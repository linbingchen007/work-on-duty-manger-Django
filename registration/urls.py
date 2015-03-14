from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'registration.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','mysite.views.index',name='index'),
    url(r'^dj/',include('mysite.urls',namespace='dj')),
)
