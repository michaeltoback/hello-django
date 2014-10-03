#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from hello.api import LegislatorResource

legislator_resource = LegislatorResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'hello.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ajax/',  'hello.views.ajax', name='ajax'),
    url(r'^api/', include(legislator_resource.urls)),
)
