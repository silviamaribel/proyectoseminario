from django.conf.urls import patterns, include, url
from django.contrib import admin
from proyectojuego.apps.inicio.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyectojuego.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include("proyectojuego.apps.inicio.urls"))
)
