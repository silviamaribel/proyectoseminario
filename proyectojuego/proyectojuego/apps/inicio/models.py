from django.db import models
from django.contrib.auth.models import User
from thumbs import ImageWithThumbsField
# Create your models here.
class Perfil(models.Model):	
	user=models.OneToOneField(User,unique=True)
	avatar=ImageWithThumbsField(upload_to="img_user",sizes=((50,50),(200,200)))
