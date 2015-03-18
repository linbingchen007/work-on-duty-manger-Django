#-*- coding:utf-8 -*-
from django.conf.urls import patterns,include,url
from mysite import views

urlpatterns=patterns('',
	url('^$',views.index,name='index'),
	url('^dj$',views.index,name='dj'),
	url('^duty$',views.duty,name='duty'),
	url('^extrawork$',views.extrawork,name='extrawork'),
	url('^holiduty$',views.holiduty,name='holiduty'),
	url('^handleholiduty',views.handleholiduty,name='handleholiduty'),
	url('^handleduty$',views.handleduty,name='handleduty'),
	url('^handleextrawork$',views.handleextrawork,name='handleextrawork'),
	url('^admin$',views.admin,name='admin'),
	url('^init$',views.init,name='init'),
	url('^login$',views.login,name='login'),
	url('^handlelogin$',views.handlelogin,name='handlelogin'),
	url('^gettable$',views.gettable,name='gettable'),
	url('^generate_data$',views.generate_data,name='generate_data'),
	url('^down$',views.down,name='down'),
	url('^chgpass$',views.chgpass,name='chgpass')
)
