from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    
     # metodos en los modelos
    def __str__(self):
        return self.nombre