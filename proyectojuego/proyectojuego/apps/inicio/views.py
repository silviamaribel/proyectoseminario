from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *

from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout

# Create your views here.
def pagina_principal(request):
	return render_to_response("inicio.html",{},RequestContext(request))
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
	return render_to_response("registrar.html",{'formulario':formulario_registro},context_instance=RequestContext(request))

def login_view(request):
	if request.method=="POST":
		formulario=AuthenticationForm(request.POST)
		if request.session['cont']>3:
			formulario2=fcapcha(request.POST)
			if formulario2.is_valid():
				pass
			else:
				datos={'formulario':formulario,'formulario2':formulario2}
				return render_to_response("login.html",datos,context_instance=RequestContext(request))
		if formulario.is_valid:
			usuario=request.POST['username']
			contrasena=request.POST['password']
			acceso=authenticate(username=usuario,password=contrasena)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
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
				return render_to_response("login.html",datos,context_instance=RequestContext(request))
	else:
		request.session['cont']=0
		formulario=AuthenticationForm()
	return render_to_response("login.html",{'formulario':formulario},context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")

def perfil_view(request):
	return render_to_response("perfil.html",{},context_instance=RequestContext(request))

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
			return render_to_response("activo.html",{'formulario':formulario},context_instance=RequestContext(request))
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
				return HttpResponseRedirect("/perfil/"+str(usuario.id)+"/")
		else:
			formulario=fperfil_modificar(instance=perfil)
			return render_to_response('modificar_perfil.html',{'formulario':formulario},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")
def lista_usuarios(request):
	usuarios=User.objects.all()
	return render_to_response("usuario/lista_usuarios.html",{"usuarios":usuarios},context_instance=RequestContext(request))
def addCategoria(request):
	usuario=request.user
	if(not usuario.has_perm("usuario.addCategoria")):
		return HttpResponseRedirect("/error/permit")
	if(request.method=="POST"):
		form_cat=Categorias_Form(request.POST)
		if(form_cat.is_valid()):
			form_cat.save()
			return HttpResponseRedirect("/blog/categoria/")
	form_cat=Categorias_Form()
	return render_to_response("blog/categorias.html",{"form":form_cat},RequestContext(request))
def addPregunta(request):
	usuario=request.user
	if(not usuario.has_perm("usuario.addPregunta")):
		return HttpResponseRedirect("/error/permit")
	if(request.method=="POST"):
		form_pre=Pregunta_Form(request.POST)
		if(form_pre.is_valid()):
			form_pre.save()
			return HttpResponseRedirect("/blog/preguntas/")
	form_pre=Pregunta_Form()
	return render_to_response("blog/preguntas.html",{"form":form_pre},RequestContext(request))


def addRespuesta(request):
	usuario=request.user
	if(not usuario.has_perm("usuario.addRespuesta")):
		return HttpResponseRedirect("/error/permit")
	if(request.method=="POST"):
		form_res=Respuestas_Opcionales_Form(request.POST)
		if(form_res.is_valid()):
			form_res.save()
			return HttpResponseRedirect("/blog/respuestas/")
	form_res=Respuestas_Opcionales_Form()
	return render_to_response("blog/respuestas.html",{"form":form_res},RequestContext(request))

def listar_usuario(request):
	usuarios=User.objects.all()
	return render_to_response("blog/listar_usuario.html",{"usuarios":usuarios},context_instance=RequestContext(request))
#def permisos(request):
#	listadepermisos=[]
#	if(request.user.has_perm("usuarios.addCategoria")):
#		listadepermisos.append("url":"/blog/categorias","label":"Categorias")
#	if(request.user.has_perm("usuarios.addPregunta")):
#		listadepermisos.append("url":"/blog/pregunta","label":"Pregunta")
#	if(request.user.has_perm("usuarios.addRespuesta")):
#		listadepermisos.append("url":"/blog/respuestas","label":"Respuestas")
#	if(request.user.has_perm("usuarios.ver_blog")):
#		listadepermisos.append("url":"/blog/addcrearpartida","label":"blog")
#	listadepermisos.append({"url":"/blog/","label":"Registro"})
#	listadepermisos.append({"url":"/blog/","label":"Login"})
# 	return listadepermisos

#preguntas

def ver_preguntas(request):
	lista=Pregunta.objects.all()
	return render_to_response("blog/ver_preguntas.html",{"lista":lista},RequestContext(request))
def restringir_categoria(request):
	lista=categoria.objects.all()
	return render_to_response("blog/restringir_categoria.html",{"categoria":categoria},RequestContext(request))
def restringir_pregunta(request):
	lista=pregunta.objects.all()
	return render_to_response("blog/restringir_pregunta.html",{"lista":lista},RequestContext(request))
def ver_categoria(request):
	lista=categorias.objects.all()
	return render_to_response("blog/ver_categoria.html",{"lista":lista},RequestContext(request))
def controlar_preguntas(request):
	lista=pregunta.objects.all()
	return render_to_response("blog/controlar_preguntas.html",{"lista":lista},RequestContext(request))

def modificar_pregunta(request,id):
	pregunta=Pregunta.objects.get(pk=id)
	if request.method=="POST":
		fpregunta=Pregunta_Form(request.POST, instance=pregunta)
		if fpregunta.is_valid():
			fpregunta.save()
			return HttpResponse("pregunta modificada")
	else:
		fpregunta=Pregunta_Form(instance=pregunta)
	return render_to_response("blog/modificar_pregunta.html",{"fpregunta":fpregunta},RequestContext(request))
#error desde aki hasta
def detalle_pregunta(request):
	pregunta=get_object_or_404(Pregunta,pk=pregunta)
	return render_to_response("blog/detalle_pregunta.html",{"pregunta":pregunta},RequestContext(request))
def ver_detalle(request,id):
	pregunta=get_object_or_404(mpregunta,pk=id)
	return render_to_response("blog/ver_detalle.html",{"pregunta":pregunta},RequestContext(request))

def ver_detalle_prgunta(request,id):
	pregunta=get_object_or_404(pregunta, pk=id)
	return render_to_response("blog/ver_detalle.html",{"pregunta":pregunta},RequestContext(request))
#eeror al eliminar 
def eliminar_pregunta(request,id):
	elim=pregunta.objects.get(pk=id)
	borrar=elim.delete()
	return render_to_response("/blog/eliminar_pregunta/")
def eliminar_lista_preguntas(request):
	lista=pregunta.objects.all()
	return render_to_response("blog/eliminar_lista_preguntas.html",{"lista":lista},RequestContext(request))
#hasta aki
def addPartida(request):
	if(request.method=="POST"):
		usuario=User.objects.get(username=request.user)
		form=PartidaForm(request.POST)
		if(form.is_valid()):
			obj=form.save(commit=False)
			obj.usuario=usuario
			obj.save()
			form.save_m2m()
			return HttpResponseRedirect("/trivia/")
	else:
		form=PartidaForm()
	return render_to_response("blog/addPartida.html",{"form":form},RequestContext(request))
def lista_de_partidas(request):
	lista=Partida.objects.filter(tipo_partida='public')
	return render_to_response("blog/lista_de_partidas.html",{"lista":lista},RequestContext(request))

