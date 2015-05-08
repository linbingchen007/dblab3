# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from mysite import views

urlpatterns = patterns('',
                       url(r'^$',views.index,name='index'),
                       url(r'^addfilm$',views.addfilm,name='addfilm'),
                       url(r'^handleaddfilm$',views.handleaddfilm,name='handleaddfilm'),
                       url(r'^getfilm/(?P<id>[0-9]+)$',views.getfilm,name='getfilm'),
                       url(r'^reg$',views.reg,name='reg'),
                       url(r'^handlereg$',views.handlereg,name='handlereg'),
                       url(r'^account$',views.account,name='account'),
                       url(r'^logout$',views.logout,name='logout'),
                       url(r'^login$',views.login,name='login'),
                       url(r'^handlelogin$',views.handlelogin,name='handlelogin'),
                       url(r'^reg/(?P<bossid>[0-9]+)$',views.regwithid,name='regwithid'),
                       url(r'^edit$',views.edit,name='edit'),
                       url(r'^handledit$',views.handledit,name='handledit'),
                       url(r'^film_list/(?P<page>[0-9]+)$',views.film_list,name='film_list'),
                       url(r'^gopagefilm$',views.gopagefilm,name='gopagefilm'),
                       
                       )