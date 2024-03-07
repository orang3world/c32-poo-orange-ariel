from django.shortcuts import render
from .models import Usuario

# Create your views here.
def userCreate(request):
    # asignarle directamente los valores a la instancia
    usuario = Usuario.objects.create(
        userName = "Marcos",
        password = "123456789"
    )
    return render(request, 'login.html', {'usuario': usuario})