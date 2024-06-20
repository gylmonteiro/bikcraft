from django.urls import path
from . import views

urlpatterns = [
   path('cadastrar/', views.cadastrar_usuario, name='cadastra-usuario'),
   path('', views.acessar, name='acessar'),
   path('sair/', views.sair, name='sair')
]
