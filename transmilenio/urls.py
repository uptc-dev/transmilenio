from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stations/', include('stations.urls')),
    path('sectors/', include('sectors.urls')),
    path('troncales/', include('trunk.urls')),
    path('tracks/', include('tracks.urls')),
    path('limits/', include('limits.urls')),
    path('transfers/', include('transfers.urls')),
    path('tracks/', include('tracks.urls')),
    path('login/', views.login),
    path('logout/', views.logout),
]
