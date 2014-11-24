from django.db import models
from thumbs import ImageWithThumbsField
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):	
	user=models.OneToOneField(User,unique=True)
	avatar=ImageWithThumbsField(upload_to="imagenusuario",sizes=((50,50),(200,200)))
class Categorias(models.Model):
	nombre=models.CharField(max_length=100)
	def __unicode__(self):
		return "->%s "%(self.nombre)
class Pregunta(models.Model):
	Titulo=models.CharField(max_length=150)
	respuesta=models.CharField(max_length=150)
	categoria=models.ManyToManyField(Categorias)
	def __unicode__(self):
		return "->%s "%(self.Titulo)
class Respuestas_Opcionales(models.Model):
	resp1=models.CharField(max_length=150)
	resp2=models.CharField(max_length=150)
	resp3=models.CharField(max_length=150)
	resp4=models.CharField(max_length=150)
	pregunta=models.ForeignKey(Pregunta)
class Juego_user(models.Model):
	part_perdido=models.IntegerField()
	part_ganado=models.IntegerField()
	puntuacion=models.IntegerField()
class Partida(models.Model):
	Titulo_p=models.CharField(max_length=150)
	Tipo=models.CharField(max_length=15)
	Num_preguntas=models.IntegerField()
	categoria_par=models.ManyToManyField(Categorias)
	usuario=models.ForeignKey(User)