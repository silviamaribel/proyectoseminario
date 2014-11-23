#encoding:utf-8
from django.forms import ModelForm
from django import forms
import pdb
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from captcha.fields import ReCaptchaField

class fcapcha(forms.Form):
    captcha = ReCaptchaField(attrs={'theme' : 'clean'})
class fperfil(ModelForm):
	nombre=forms.CharField(max_length=100)
	apellidos=forms.CharField(max_length=100)
	class Meta:
		model=Perfil
		exclude=['user']
class fperfil_modificar(ModelForm):
	class Meta:
		model=Perfil
		exclude=['user']

class fusuario(UserCreationForm):
	username=forms.CharField(max_length=40,required=True,help_text=False,label="Nick")
	password2=forms.CharField(help_text=False,label="Contraseña de confirmación", widget=forms.PasswordInput)
	first_name=forms.CharField(max_length=50,required=True,label="Nombre")
	email=forms.EmailField(max_length=100,required=True,label="Email")
	class Meta:
		model=User
		fields=("username","password1","password2","first_name","email")
	def save(self, commit=True):
		user=super(fusuario,self).save(commit=False)
		user.first_name=self.cleaned_data.get("first_name")
		user.email=self.cleaned_data.get("email")
		if commit:
			user.save()
		return user
class Categorias_Form(ModelForm):
	class Meta:
		model=Categorias
class Pregunta_Form(ModelForm):
	class Meta:
		model=Pregunta
class Respuestas_Opcionales_Form(ModelForm):
	class Meta:
		model=Respuestas_Opcionales
		#exclude=["pregunta"]
class PartidaForm(ModelForm):
	#tipo_partida=forms.ChoiceField(widget=forms.RadioSelect,choices=tipo)
	#seleccionar_categoria=forms.ModelMultipleChoiceField(queryset=categoria.objects.all(),widget=forms.CheckboxSelectMultiple())
	class Meta:
		model=Partida
		exclude=["usuario"]