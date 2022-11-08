from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar

# Create your views here.
# def mostrar_curso(request):
#     curso = Curso(nombre='Python', comision='34635')
#     saludo = f'Hola a la todos, este es el curso de {curso.nombre}, con numero de comision: {curso.comision}'
#     return HttpResponse(saludo)

def mostrar_familiares(request):
    listaFamiliares = Familiar.objects.all()
    return render(request, 'familiares.html', {"data": listaFamiliares})