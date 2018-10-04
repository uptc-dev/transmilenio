from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.trunks),
    url(r'^(?P<pk>\d+)$', views.trunk),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
