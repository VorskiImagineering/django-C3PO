#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='c3po_index')
                       )
