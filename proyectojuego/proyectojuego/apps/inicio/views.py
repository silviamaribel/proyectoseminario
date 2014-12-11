from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *

from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.sessions.backends.db import SessionStore

# Create your views here.
def pagina_principal(request):
	return render_to_response("usuario/inicio.html",{},RequestContext(request))
def pagina_admin(request):
	return render_to_response("perfilAd.html",{},RequestContext(request))
def registro_view(request):
	if request.method=="POST":
		formulario_registro=fusuario(request.POST)
		if formulario_registro.is_valid():
			nuevo_usuario=request.POST['username']
			formulario_registro.save()
			usuario=User.objects.get(username=nuevo_usuario)
			usuario.is_active=False
			usuario.save()
			perfil=Perfil.objects.create(user=usuario)
			return HttpResponse("Registrado con exito")
	else:
		formulario_registro=fusuario()
	return render_to_response("usuario/registrar.html",{'formulario':formulario_registro},context_instance=RequestContext(request))

def login_view(request):
	if request.method=="POST":
		formulario=AuthenticationForm(request.POST)
		if request.session['cont']>3:
			formulario2=fcapcha(request.POST)
			if formulario2.is_valid():
				pass
			else:
				datos={'formulario':formulario,'formulario2':formulario2}
				return render_to_response("usuario/login.html",datos,context_instance=RequestContext(request))
		if formulario.is_valid:
			usuario=request.POST['username']
			contrasena=request.POST['password']
			acceso=authenticate(username=usuario,password=contrasena)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					p=SessionStore()
					p["name"]=usuario
					p["estado"]="conectado"
					p.save()
					request.session["idkey"]=p.session_key
					del request.session['cont']
					return HttpResponseRedirect("/user/perfil/")
				else:
					login(request, acceso)
					
					return HttpResponseRedirect("/user/active/")
			else:
				request.session['cont']=request.session['cont']+1
				aux=request.session['cont']
				estado=True
				mensaje="Error en los datos "+str(aux)
				if aux>3:
					formulario2=fcapcha()
					datos={'formulario':formulario,'formulario2':formulario2,'estado':estado,'mensaje':mensaje}
				else:
					datos={'formulario':formulario,'estado':estado,'mensaje':mensaje}
				return render_to_response("usuario/login.html",datos,context_instance=RequestContext(request))
	else:
		request.session['cont']=0
		formulario=AuthenticationForm()
	return render_to_response("usuario/login.html",{'formulario':formulario},context_instance=RequestContext(request))

def logout_view(request):
	#p=SessionStore(session_key=request.session["idkey"])
	#p["estado"]="desconectado"
	#p["name"]=""
	#p.save()
	logout(request)
	return HttpResponseRedirect("/login/")
def chat(request):
	idsession=request.session["idkey"]
	return HttpResponseRedirect("http://localhost:3000/django/"+idsession)

def perfil_view(request):
	usuario=User.objects.get(username=request.user)
	# try:
	# 	perfil=Perfil.objects.get(user=usuario)
	# 	return HttpResponseRedirect("/user/perfil/")
	# except Perfil.DoesNotExist:
	# 		usuario_nuevo=User.objects.get(username=usuario)
	# 		perfil=Perfil.objects.create(user=usuario_nuevo)
#creas y le envias a su perfil
	return render_to_response("usuario/perfil.html",{},context_instance=RequestContext(request))

def user_active_view(request):
	if request.user.is_authenticated():
		usuario=request.user
		if usuario.is_active:
			return HttpResponseRedirect("/user/perfil/")
		else:
			if request.method=="POST":
				u=User.objects.get(username=usuario)
				perfil=Perfil.objects.get(user=u)
				formulario=fperfil(request.POST,request.FILES,instance=perfil)
				if formulario.is_valid():
					formulario.save()
					u.is_active=True
					u.save()
					return HttpResponseRedirect("/user/perfil/")
			else:
				formulario=fperfil()
			return render_to_response("usuario/activo.html",{'formulario':formulario},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")
def modificar_perfil(request):
	if request.user.is_authenticated():
		u=request.user
		usuario=User.objects.get(username=u)
		perfil=Perfil.objects.get(user=usuario)
		if request.method=='POST':
			formulario=fperfil_modificar(request.POST,request.FILES,instance=perfil)
			if formulario.is_valid():
				formulario.save()
				return HttpResponseRedirect("/user/perfil/")
		else:
			formulario=fperfil_modificar(instance=perfil)
			return render_to_response('usuario/modificar_perfil.html',{'formulario':formulario},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")
def listausuarios(request):
	usuarios=User.objects.all()
	return render_to_response("usuario/listausuarios.html",{"usuarios":usuarios},context_instance=RequestContext(request))
def listar_usuario(request):
	usuarios=User.objects.all()
	return render_to_response("blog/listar_usuario.html",{"usuarios":usuarios},context_instance=RequestContext(request))


def registro_tema(request):
	usuario=request.user
	if(not usuario.has_perm("usuario.addTema")):
		return HttpResponseRedirect("/error/permit")
	titulo="Regitro de temas"
	temas=Tema.objects.all()
	if request.method=="POST":
		formulario=ftema(request.POST)
		if formulario.is_valid():
			formulario.save()
			estado=True
			datos={'titulo':titulo,'formulario':formulario,'estado':estado,'temas':temas}
			return render_to_response("pregunta/registro_temas.html",datos,context_instance=RequestContext(request))
	else:
		formulario=ftema()
	datos={'titulo':titulo,'formulario':formulario,'temas':temas}
	return render_to_response("pregunta/registro_temas.html",datos,context_instance=RequestContext(request))

def add_pregunta(request,id):
	tema=Tema.objects.get(id=int(id))
	titulo="Registrar pregunta para el tema de "+tema.nombre
	titulo2="Registre las respuestas"
	if request.method=="POST":
		formulario=fpregunta(request.POST)
		formulario2=frespuesta(request.POST)
		if formulario.is_valid() and formulario2.is_valid():
			pregunta=formulario.save(commit=False)
			pregunta.tema=tema
			pregunta.save()
			respuesta=formulario2.save(commit=False)
			respuesta.pregunta=pregunta
			respuesta.save()
			estado=True
			formulario=fpregunta()
			datos={'titulo':titulo,'formulario':formulario,'estado':estado,'titulo2':titulo2,'formulario2':formulario2}
			return render_to_response("pregunta/registro_preguntas.html",datos,context_instance=RequestContext(request))
	else:
		formulario=fpregunta()
		formulario2=frespuesta()
	datos={'titulo':titulo,'titulo2':titulo2,'formulario':formulario,'formulario2':formulario2}
	return render_to_response("pregunta/registro_preguntas.html",datos,context_instance=RequestContext(request))
def ver_preguntas(request,id):
	tema=Tema.objects.get(id=int(id))
	preguntas=Pregunta.objects.filter(tema=tema)
	datos={'tema':tema,'preguntas':preguntas}
	return render_to_response("pregunta/ver_preguntas.html",datos,context_instance=RequestContext(request))

def edit_pregunta(request,id):
	pregunta=Pregunta.objects.get(id=int(id))
	respuesta=Respuesta.objects.get(pregunta=pregunta)
	titulo="Editar pregunta"
	titulo2="Editar las respuestas"
	if request.method=="POST":
		formulario=fpregunta(request.POST,instance=pregunta)
		formulario2=frespuesta(request.POST,instance=respuesta)
		if formulario.is_valid() and formulario2.is_valid():
			formulario.save()
			formulario2.save()
			estado=True
			datos={'titulo':titulo,'formulario':formulario,'estado':estado,'titulo2':titulo2,'formulario2':formulario2}
			return render_to_response("pregunta/registro_preguntas.html",datos,context_instance=RequestContext(request))
	else:
		formulario=fpregunta(instance=pregunta)
		formulario2=frespuesta(instance=respuesta)
	datos={'titulo':titulo,'titulo2':titulo2,'formulario':formulario,'formulario2':formulario2}
	return render_to_response("pregunta/registro_preguntas.html",datos,context_instance=RequestContext(request))

def eliminar_pregunta(request,id):
	pregunta=Pregunta.objects.get(id=int(id))
	id=pregunta.tema.id
	respuesta=Respuesta.objects.get(pregunta=pregunta)
	pregunta.delete()
	respuesta.delete()
	return HttpResponseRedirect("/tema/edit/"+str(id)+"/")
def error_permisos(request):
	return render_to_response("error_permisos.html",{},RequestContext(request))
def crear_partida(request):
	if (request.method=="POST"):
		usuario=User.objects.get(username=request.user)
		form=partidaForm(request.POST)
		#usuario=User.objects.get(username=request.user)
		if(form.is_valid()):
			obj=form.save(commit=False)
			obj.usuario=usuario
			obj.save()
			form.save_m2m()
			return HttpResponse("creado con exito")
	else:
		form=partidaForm()
	return render_to_response("pregunta/crearpartida.html",{"form":form},RequestContext(request))
def lista_partidas(request):
	lista=partida.objects.filter(tipo_partida='public')
	return render_to_response("pregunta/listapartidas.html",{"lista":lista},RequestContext(request))




