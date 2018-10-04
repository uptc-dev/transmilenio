from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.sectors),
    url(r'^(?P<pk>\d+)$', views.sector),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
