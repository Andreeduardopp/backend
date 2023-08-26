from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.utils import valida_telefone
class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    celular = models.CharField(max_length=30,blank=True, validators=[valida_telefone])
    foto_perfil = models.ImageField(upload_to='media/usuario/perfil', blank=True, null=True)
    foto_background = models.ImageField(upload_to='media/usuario/background', blank=True, null=True)
