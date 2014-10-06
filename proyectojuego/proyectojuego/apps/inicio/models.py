from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Perfil(models.Model):	
	user=models.OneToOneField(User,unique=True)
	pais=models.CharField(max_length="30", null=False)