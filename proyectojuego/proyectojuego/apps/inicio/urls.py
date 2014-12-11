from django.conf.urls import patterns, include, url
from proyectojuego.apps.inicio.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chatgrafico.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', pagina_principal),
  url(r'^inicio/$',pagina_principal), 
	url(r'^user/registro/$',registro_view),
	url(r'^login/$',login_view), 
	url(r'^logout/$',logout_view), 
	url(r'^user/perfil/$',perfil_view),
	url(r'^user/active/$',user_active_view),
	url(r'^user/modificar/$',modificar_perfil),
  url(r'^actualizar/$',registro_view),
  url(r'^perfilad/$',pagina_admin),
  url(r'^listausuarios/$',listausuarios),
  url(r'^registro/tema/$',registro_tema, name='Tema'),
  url(r'^tema/add/(\d+)/$',add_pregunta, name='agregar_pregunta'),
  url(r'^tema/edit/(\d+)/$',ver_preguntas, name='edit_pregunta'),
  url(r'^pregunta/edit/(\d+)/$',edit_pregunta, name='edit_pregunta'),
  url(r'^pregunta/eliminar/(\d+)/$',eliminar_pregunta, name='eliminar_pregunta'),
  url(r'^crearpartida/$',crear_partida),
  url(r'^listapartidas/$',lista_partidas),
  url(r'^error/permit/$',error_permisos),
  url(r'^chat/$',chat),
  
)