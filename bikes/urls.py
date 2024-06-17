from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="pagina-inicial"),
    path("cadastrar/", views.cadastrar, name="cadastra-bike"),
    path("bikes/", views.listar_bikes, name="listar-bikes"),
    path('lojas/', views.listar_lojas, name='listar-lojas' ),
    path('lojas/cadastrar', views.cadastrar_loja, name='cadastra-loja'),
    path('lojas/detalhes/<int:id>/', views.detalha_loja, name='detalha-loja'),
    path('vendedores/', views.listar_vendedores, name='lista-vendedores'),
    path('vendedores/cadastrar', views.cadastrar_vendedor, name='cadastra-vendedor'),
    path("contato/", views.contact_view, name="contato"),
]
