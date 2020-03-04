from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    return render(request,'usuarios/cadastro.html')

def loguin(request):
    return render(request,'usuarios/usuarios.html')

def deshborad(request):
    pass

def logout(request):
    pass

