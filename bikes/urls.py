from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="pagina-inicial"),
    path("cadastrar/", views.cadastrar, name="cadastra-bike"),
    path("deletar_bike/<int:pk>/", views.deletar_bike, name="deleta-bike"),
    path("bikes/", views.ListarBikesListView.as_view(), name="listar-bikes"),
    path("bikes/update/<int:pk>/", views.UpdateBikeView.as_view(), name='atualiza-bike'),
    path("lojas/", views.ListarLojasView.as_view(), name="listar-lojas"),
    path("lojas/cadastrar", views.CadastrarLojaView.as_view(), name="cadastra-loja"),
    path("lojas/detalhes/<int:pk>/", views.DetalheLojaView.as_view(), name="detalha-loja"),
    path('lojas/atualizar/<int:pk>/',views.AtualizarLojaView.as_view(), name='atualizar-loja'),
    path('lojas/deletar/<int:pk>/', views.DeletarLojaView.as_view(), name='deletar-loja'),
    path("vendedores/", views.listar_vendedores, name="lista-vendedores"),
    path("vendedores/cadastrar/", views.cadastrar_vendedor, name="cadastra-vendedor"),
    path("venderores/atualizar/<int:pk>/", views.atualizar_vendedor, name='atualiza-vendedor'),
    path("contato/", views.contact_view, name="contato"),
]
