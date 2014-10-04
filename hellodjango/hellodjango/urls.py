#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from hello.api import LegislatorResource, TermsResource

legislator_resource = LegislatorResource()
terms_resource = TermsResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'hello.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ajax/',  'hello.views.ajax', name='ajax'),
    url(r'^api1/', include(terms_resource.urls,)),
    url(r'^api2/', include(legislator_resource.urls,)),
)
