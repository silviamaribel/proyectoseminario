from django.conf.urls import patterns, include, url
from django.contrib import admin
from proyectojuego.apps.inicio.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chatgrafico.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', pagina_principal), 
	url(r'^user/registro/$',registro_view),
	url(r'^login/$',login_view), 
	url(r'^logout/$',logout_view), 
	url(r'^user/perfil/$',perfil_view),
	url(r'^user/active/$',user_active_view),
)