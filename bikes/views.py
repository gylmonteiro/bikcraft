from django.shortcuts import render, redirect
from .forms import BikeModelForm
from .models import Bike


# Create your views here.
def home(request):
   
    return render(request, 'home.html')


def cadastrar(request):
    
    if request.method == 'POST':
        bike_form = BikeModelForm(request.POST, request.FILES)
        if bike_form.is_valid():
            bike_form.save()
            return redirect ('pagina-inicial')
    else:
        bike_form = BikeModelForm()
    return render(request, 'formulario_bike.html', {'form': bike_form})


def listar_bikes(request):
    bikes = Bike.objects.all()
    return render (request, 'produtos.html', {'bikes': bikes})

