from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from receitaap.models import Receitas
from django.contrib import auth, messages


def index(request):
    receitas = Receitas.objects.order_by('-data_receite').filter(publicada = True)
    
    dados = {
        'receitas' :receitas
    }
    return render(request,'receitas/index.html',dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)
    receita_exibir = {
        'receita':receita
    }
    return render(request,'receitas/receita.html',receita_exibir)

def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receitas.objects.create(pessoa=user, nome_receita=nome_receita, ingredientes=ingredientes,
                                         mode_de_preparo=modo_preparo, tempo_de_preparo=tempo_preparo, rendimento=rendimento,
                                         categoria=categoria, foto_receita=foto_receita)
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'receitas/cria_receita.html')

def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receitas,pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def edita_receita(request,receita_id):
    receita = get_object_or_404(Receitas,pk=receita_id)
    receita_editar = {'receita':receita}
    return render(request,'receitas/edita_receitas.html',receita_editar)

def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        r = Receitas.objects.get(pk=receita_id)
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            r.foto_receita = request.FILES['foto_receita']
        r.save()
        return redirect('dashboard')