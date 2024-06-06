from django.shortcuts import render, redirect
from .forms import BikeForm


# Create your views here.
def home(request):
   
    return render(request, 'home.html')


def cadastrar(request):
    
    if request.method == 'POST':
        bike_form = BikeForm(request.POST, request.FILES)
        if bike_form.is_valid():
            bike_form.save()
            return redirect ('pagina-inicial')
    else:
        bike_form = BikeForm()
    return render(request, 'formulario_bike.html', {'form': bike_form})

