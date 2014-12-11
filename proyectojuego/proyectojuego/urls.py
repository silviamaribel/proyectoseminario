from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyectojuego.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('proyectojuego.apps.inicio.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    {'document_root':settings.MEDIA_ROOT,}
    ),
    #facebook
    url('', include('social.apps.django_app.urls',namespace='social')),
    url('', include('django.contrib.auth.urls',namespace='auth')),
)
