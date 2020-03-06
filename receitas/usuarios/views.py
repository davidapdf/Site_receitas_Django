from django.contrib import auth
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip() or not email.strip() or not senha.strip() or not senha2.strip():
            print('Campos não podem ficar em branco')
        if User.objects.filter(email=email).exists():
            print('usuario ja cadastrado')
            return redirect('cadastro')
        else:
            user = User.objects.create_user(username=nome,email=email,password=senha)
            user.save()
            print('usuario cadastrado')
            return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print('Os campos não podem ficar em branco')
            return redirect('login')
        print(senha,email)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username',flat=True).get()
            user = auth.authenticate(request,username=nome,password=senha)

            if user is not None:
                auth.login(request,user)
                print("login realizado com sucesso")
                return redirect('dashboard')
        return redirect('dashboard')
    return render(request,'usuarios/login.html')

def dashboard(request):
    return render(request,'usuarios/dashboard.html')

def logout(request):
    pass

