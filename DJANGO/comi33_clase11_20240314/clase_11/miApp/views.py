from django.shortcuts import render
from .models import User
# Create your views here.
def helloUser(request):
    usuario = User.objects.create(
    nombre = "Juan"
    )
    return render(
        request,
        'hello.html',
        {'nombre_usuario': usuario.nombre}
    )