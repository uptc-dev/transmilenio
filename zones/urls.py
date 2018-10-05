# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.zones),
    url(r'^(?P<pk>\d+)$', views.zone),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
