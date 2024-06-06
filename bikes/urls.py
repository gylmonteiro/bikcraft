from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pagina-inicial'),
    path('cadastrar/', views.cadastrar, name='cadastra-bike')
]
