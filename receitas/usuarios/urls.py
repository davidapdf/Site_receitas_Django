from django.urls import path
from . import views

urlpatterns = [
    path('cadastro',views.cadas,name = 'cadastro'),
    path('loguin',views.loguin,name = 'loguin'),
    path('deshborad',views.deshborad,name = 'deshborad'),
    path('logout',views.logout,name = 'logout')
]