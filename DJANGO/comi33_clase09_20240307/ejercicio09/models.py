from pyexpat import model
from django.db import models

# Create your models here.
class Usuario(models.Model):
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=10)

    class Meta:
        ordering = ['-userName']
    def __str__(self):
        return self.userName