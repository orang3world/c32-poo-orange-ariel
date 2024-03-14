from django.shortcuts import render
from .models import Estudiante
# Create your views here.
"""CRUD
C CREATE
R READ
U UPDATE
D DELETE"""


# Creacion de un estudiante
def crearEstudiante(request):
    ingreso = Estudiante.objects.create(
        nombre= 'Jose',
        apellido='Altamirano',
        edad=25,
        nota=8,
    )
    return render(request, 'lista.html', {'ingreso': ingreso})