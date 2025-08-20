from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    titulo_slug = models.SlugField(unique=True, blank=True)
    contenido = models.TextField()
    archivo_multimedia = models.FileField(upload_to='post_files/', blank=True, null=True) 
    fecha_creacion = models.DateTimeField(auto_now_add= True)
    
    def save(self, *args, **kwargs):
        if not self.titulo_slug:
            self.titulo_slug = slugify(self.titulo)
        super().save(*args, **kwargs)


class Comentario(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add= True)

from django.db import models
from django.utils.text import slugify
