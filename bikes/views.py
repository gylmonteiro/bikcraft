from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .forms import BikeModelForm,LojaModelForm, VendedorModelForm , ContactForm, ContactFormSet
from .models import Bike, Loja, Vendedor


# Create your views here.
def home(request):
    return render(request, 'home.html')

def cadastrar(request):
    user = request.user
    if user.is_authenticated: # Se isso for True, executa até a linha 24
        if request.method == 'POST':
            bike_form = BikeModelForm(request.POST, request.FILES)
            if bike_form.is_valid(): # -> se isso der errado, abaixo não executa
                # Isso não é mais executado
                bike_form.save()
                return redirect("listar-bikes")
        else:
            bike_form = BikeModelForm()
        return render(request, 'formulario_bike.html', {'form': bike_form})
    # Se user não tiver auntenticado... Joga ele pra pagina inicial
    else:
        return redirect("acessar")

def listar_bikes(request):
    bikes = Bike.objects.all()
    return render (request, 'produtos.html', {'bikes': bikes})


@login_required
def cadastrar_loja(request):

    if request.method == 'POST':
        loja_form = LojaModelForm(request.POST)

        if loja_form.is_valid():
            loja_form.save()

            return redirect('listar-bikes')

    loja_form = LojaModelForm()
    return render(request, 'formulario_loja.html', {'form': loja_form} )


def listar_lojas(request):
    lojas = Loja.objects.all()
    return render(request, 'lojas.html', {'lojas': lojas})


def detalha_loja(request, id):
    loja = get_object_or_404(Loja, pk=id)
    return render(request, "detalhe_loja.html", {"loja": loja})

@login_required
def cadastrar_vendedor(request):

    if request.method == 'POST':
        vendedor_form = VendedorModelForm(request.POST)
        if vendedor_form.is_valid():
            vendedor_form.save()

            return redirect("lista-vendedores")

    vendedor_form = VendedorModelForm()
    return render(request, 'formulario_vendedor.html', {'form': vendedor_form})


def listar_vendedores(request):
    vendedores = Vendedor.objects.all()

    return render(request, 'vendedores.html', {'vendedores': vendedores})


def contact_view(request):
    if request.method == "POST":
        form = ContactFormSet(request.POST)
        if form.is_valid():
            # Processar os dados do formulário
            pass
    else:
        form = ContactFormSet()

    return render(request, "contact.html", {"form": form})
