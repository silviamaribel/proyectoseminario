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
	logout(request)
	return HttpResponseRedirect("/login/")

def perfil_view(request):
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
def agregarCategoria(request):
	usuario=request.user
	if(not usuario.has_perm("usuario.addCategoria")):
		return HttpResponseRedirect("/error/permit")
	if(request.method=="POST"):
		form_cat=Categorias_Form(request.POST)
		if(form_cat.is_valid()):
			form_cat.save()
			return HttpResponseRedirect("/categoria/")
	form_cat=Categorias_Form()
	return render_to_response("categoria.html",{"form":form_cat},RequestContext(request))
def agregarPregunta(request):
	usuario=request.user
	if(not usuario.has_perm("usuario.agregarPregunta")):
		return HttpResponseRedirect("/error/permit")
	if(request.method=="POST"):
		form_pre=Pregunta_Form(request.POST)
		if(form_pre.is_valid()):
			form_pre.save()
			return HttpResponseRedirect("/preguntas/")
	form_pre=Pregunta_Form()
	return render_to_response("preguntas.html",{"form":form_pre},RequestContext(request))


def agregarRespuesta(request):
	usuario=request.user
	if(not usuario.has_perm("usuario.addRespuesta")):
		return HttpResponseRedirect("/error/permit")
	if(request.method=="POST"):
		form_res=Respuestas_Opcionales_Form(request.POST)
		if(form_res.is_valid()):
			form_res.save()
			return HttpResponseRedirect("/respuestas/")
	form_res=Respuestas_Opcionales_Form()
	return render_to_response("respuestas.html",{"form":form_res},RequestContext(request))


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
def modificar_pregunta(request,id):
	pregunta=get_object_or_404(mPregunta,pk=id)
	if request.method=="POST":
		fpregunta=preguntaForm(request.POST,instance=pregunta)	
		if fpregunta.is_valid():
			fpregunta.save()
			return HttpResponse("Pregunta modificada ")
	else:
		fpregunta=preguntaForm(instance=pregunta)
	return render_to_response("pregunta/modificar_preg.html",{"fpregunta":fpregunta},RequestContext(request))
def eliminar_pregunta(request,id):
	aux=Pregunta.objects.get(pk=id)
	borrar=aux.delete()
	return HttpResponseRedirect("/pregunta/preguntaseliminar/")
def listar_pregunta(request):
	pregunta=Pregunta.objects.all()
	return render_to_response("listar_pregunta.html",{'pregunta':pregunta},context_instance=RequestContext(request))

def pregunta_ver(request,id):
	lista=Pregunta.objects.all()
	return render_to_response("pregunta/ver_preg.html",{"lista":lista},RequestContext(request))

def listar_categoria(request):
	lista=Categorias.objects.all()
	return render_to_response("pregunta/ver_cat.html",{"lista":lista},RequestContext(request))











#def ver_preguntas(request):
#	lista=Pregunta.objects.all()
#	return render_to_response("pregunta/ver_preg.html",{"lista":lista},RequestContext(request))
#def ver_categoria(request):
#	lista=Categorias.objects.all()
#	return render_to_response("pregunta/ver_cat.html",{"lista":lista},RequestContext(request))
#def control_preguntas(request):
#	lista=Pregunta.objects.all()
#	return render_to_response("pregunta/controlar_preg.html",{"lista":lista},RequestContext(request))
#
#def detalle_pregunta(request):
#	lista=Pregunta.objects.all()
#	return render_to_response("pregunta/detalle_preg.html",{"lista":lista},RequestContext(request))
#def ver_detalles(request,id):
#	pregunta=get_object_or_404(Pregunta,pk=id)
#	return render_to_response("pregunta/ver_detalle.html",{"pregunta":pregunta},RequestContext(request))
#
#def lista_preguntas_eliminar(request):
#	lista=Pregunta.objects.all()
#	return render_to_response("pregunta/eliminar_list_preg.html",{"lista":lista},RequestContext(request))

