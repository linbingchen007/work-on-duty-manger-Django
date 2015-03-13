#-*- coding:utf-8 -*-
from django.conf.urls import patterns,include,url
from mysite import views

urlpatterns=patterns('',
	url('^$',views.index,name='index'),
	url('^dj$',views.index,name='dj'),
	url('^duty$',views.duty,name='duty'),
	url('^extrawork$',views.extrawork,name='extrawork'),
	url('^handleduty$',views.handleduty,name='handleduty'),
	url('^handleextrawork$',views.handleextrawork,name='handleextrawork'),
	url('^admin',views.admin,name='admin'),
)