#-*- coding:utf-8 -*-
from django.conf.urls import patterns,include,url
from mysite import views

urlpatterns=patterns('',
	url('^$',views.index,name='index'),
	url('^dj$',views.index,name='dj'),
	url('^admin',views.admin,name='admin'),
)