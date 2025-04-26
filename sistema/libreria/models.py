from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200,verbose_name="Título")
    imagen = models.ImageField(upload_to='libros/', null= True, blank= True,verbose_name="Imagen")
    descripcion = models.TextField(verbose_name="Descripción")

def __str__(self):
    
    return self.titulo

class Meta: 
        verbose_name = "Libro"  # Nombre singular en el admin 
        verbose_name_plural = "Libros"  # Nombre plural en el admin






