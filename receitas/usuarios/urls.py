from django.urls import path
from . import views

urlpatterns = [
    path('cadastro',views.cadastro,name = 'cadastro'),
    path('loguin',views.loguin,name = 'loguin'),
    path('deshborad',views.deshborad,name = 'deshborad'),
    path('logout',views.logout,name = 'logout'),
]