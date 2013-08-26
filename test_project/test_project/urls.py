#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^', include('django_c3po.urls')),
                       url(r'^login/$', 'django.contrib.auth.views.login', name='auth_login'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', name='auth_logout'),
                       url(r'^admin/', include(admin.site.urls)),
                       )
