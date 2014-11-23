from django.conf.urls import patterns, include, url
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
	url(r'^user/modificar/$',modificar_perfil),
	url(r'^categoria/$',addCategoria),
  url(r'^respuestas/$',addRespuesta),
  url(r'^preguntas/$',addPregunta),
  url(r'^actualizar/$',registro_view),
  	#url(r'^usuario_activo/$',usuario_activo),
  url(r'^lista_usuarios/$',lista_usuarios),

  url(r'^verpreguntas/$',ver_preguntas),
 	url(r'^vercategorias/$',ver_categoria),
  url(r'^restringircategoria/$',restringir_categoria),
  url(r'^restringirpregunta/$',restringir_pregunta),
  url(r'^controlarpregunta/$',controlar_preguntas),
  url(r'^detallepreguntas/$',detalle_pregunta),
  url(r'^modificar/(?P<id>\d+)/$',modificar_pregunta,name='modificar_pregunta'),
  url(r'^verdetallepregunta/(?P<id>\d+)/$',ver_detalle,name='ver_detalle'),
  url(r'^eliminarpregunta/(?P<id>\d+)/$',eliminar_pregunta,name='eliminar_pregunta'),
  url(r'^eliminarlistadepreguntas/$',eliminar_lista_preguntas),
  url(r'^crearpartida/$',addPartida),
  url(r'^listapartidas/$',lista_de_partidas),
)