from pyexpat import model
from django.db import models

# Create your models here.
class Usuario(models.Model):
    userName = models.CharField(max_lenght=100)
    password = models.CharField(max_lenght=10)

    class Meta:
        ordening = ['-userName']
    def __str__(self):
        return self.userName