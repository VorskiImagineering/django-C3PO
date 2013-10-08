#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^$',
                           views.IndexView.as_view(), name='c3po_index'),
                       url(r'^task/(?P<task_id>[0-9a-f-]+)$',
                           views.TaskStateView.as_view(), name='c3po_task'),
                       )
