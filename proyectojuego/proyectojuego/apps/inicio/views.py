from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *

from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout

# Create your views here.
def registro_view(request):
	if request.method=="POST":
		formulario_registro=fusuario(request.POST)
		if formulario_registro.is_valid():
			nuevo_usuario=request.POST['username']
			formulario_registro.save()
			usuario=User.objects.get(username=nuevo_usuario)
			perfil=Perfil.objects.create(user=usuario)
			return HttpResponse("Registrado")
	else:
		formulario_registro=fusuario()
	return render_to_response("registrar.html",{'formulario':formulario_registro},context_instance=RequestContext(request))
def login_view(request):
	if request.method=="POST":
		formulario=AuthenticationForm(request.POST)
		if(formulario.is_valid()==False):
			usuario=request.POST["username"]
			contrasena=request.POST["password"]
			acceso=authenticate(username=usuario,password=contrasena)
			if acceso:
				login(request,acceso)
				request.session["name"]=usuario
				return HttpResponseRedirect("/user/perfil/")
	formulario=AuthenticationForm()
	return render_to_response("login.html",{"formulario":formulario},RequestContext(request))
def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")

def perfil_view(request):
	return render_to_response("perfil.html",{"nombre":request.session["name"]},RequestContext(request))
def pagina_principal(request):
	return render_to_response("inicio.html",{},RequestContext(request))

