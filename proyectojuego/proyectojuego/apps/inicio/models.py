from django.db import models
from thumbs import ImageWithThumbsField
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):	
	user=models.OneToOneField(User,unique=True)
	avatar=ImageWithThumbsField(upload_to="imagenusuario",sizes=((50,50),(200,200)))

class Tema(models.Model):
	nombre=models.CharField(max_length=20,unique=True)
	def __str__(self):
		return self.nombre

class Pregunta(models.Model):
	nombre=models.CharField(max_length=500)
	tema=models.ForeignKey(Tema)
	def __str__(self):
		return self.nombre

class Respuesta(models.Model):
	respuesta_correcta=models.CharField(max_length=500)
	respusta_opcional1=models.CharField(max_length=500)
	respusta_opcional2=models.CharField(max_length=500)
	pregunta=models.ForeignKey(Pregunta)
	def __str__(self):
		return self.pregunta
# class Juego_user(models.Model):
# 	part_perdido=models.IntegerField()
# 	part_ganado=models.IntegerField()
# 	puntuacion=models.IntegerField()
# class Partida(models.Model):
# 	Titulo_p=models.CharField(max_length=150)
# 	Tipo=models.CharField(max_length=15)
# 	Num_preguntas=models.IntegerField()
# 	categoria_par=models.ManyToManyField(Categorias)
# 	usuario=models.ForeignKey(User)
# class Perfil(models.Model):
# 	user=models.OneToOneField(User, unique=True)
# 	pais=models.CharField(max_length=100, null=True)
# 	#firt_name=models.CharField(max_length=30)
# 	#last_name=models.CharField(max_length=30)
# 	avatar=ImageWithThumbsField(upload_to="img_user", sizes=((50,50),(200,200)))
