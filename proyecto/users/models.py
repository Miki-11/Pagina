from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length = 100)
    Password = models.CharField(max_length = 100)
    Email = models.EmailField(blank=True , null = True)
    def __str__(self):
        return self.username
    
class Entrada(models.Model):
   titulo = models.CharField(max_length=100)
   texto = models.TextField(null=True, blank=True)
   archivo = models.FileField(upload_to="archivos/", null=True, blank=True)


class Programa(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    tipo = models.CharField(max_length=50)
