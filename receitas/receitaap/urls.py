from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('<int:receita_id>',views.receita,name = 'receita'),
    path('busca',views.buscar,name = 'buscar'),
    path('cria/receita',views.cria_receita,name= 'cria_receita'),
    path('delete/<int:receita_id>',views.deleta_receita,name='deleta_receita'),
    path('edita/<int:receita_id>',views.edita_receita,name = 'edita_receita'),
    path('atualiza/receita',views.atualiza_receita,name ='atualiza_receita')
]
