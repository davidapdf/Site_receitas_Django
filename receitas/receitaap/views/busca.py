from django.shortcuts import render

from receitaap.models import Receitas


def buscar(request):
    lista_receitas = Receitas.objects.order_by('-data_receite').filter(publicada=True)
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }
    return render(request, 'receitas/buscar.html', dados)