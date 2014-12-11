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
class partida(models.Model):
	titulo=models.CharField(max_length=200)
	tipos=(('public','Publico'),('private','Privado'))
	cant_preguntas=(('10','10'),('20','20'),('30','30'),('40','40'),('50','50'))
	tiempo=(('10','10'),('15','15'),('20','20'),('25','25'),('30','30'),('35','35'),('40','40'),('45','45'),('50','50'),('55','55'),('60','60'))
	jugadores=models.PositiveIntegerField()
	tipo_partida=models.CharField(max_length=200,choices=tipos)
	preguntas=models.CharField(max_length=5, choices=cant_preguntas)
	tiempo_respuesta=models.CharField(max_length=5,choices=tiempo)
	temas_sel=models.ManyToManyField(Tema, blank=False)
	usuario=models.ForeignKey(User)
	def __unicode__(self):
		return self.titulos

