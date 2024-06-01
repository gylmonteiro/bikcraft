from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pagina-inicial'),
    path('produtos/', views.produtos, name='lista-produtos')
]
# Este arquivo serve para ser responsável pelos endereços de bikes