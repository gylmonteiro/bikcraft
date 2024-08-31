from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DeleteView, DetailView, CreateView, TemplateView, UpdateView
from .forms import BikeModelForm,LojaModelForm, VendedorModelForm , ContactForm, ContactFormSet
from .models import Bike, Loja, Vendedor


# Views baseadas em funções
@login_required
def cadastrar_loja(request):

    if request.method == "POST":
        loja_form = LojaModelForm(request.POST)

        if loja_form.is_valid():
            loja_form.save()

            return redirect("listar-bikes")

    loja_form = LojaModelForm()
    return render(request, "formulario_loja.html", {"form": loja_form})


@method_decorator(login_required, name="dispatch")
class CadastrarLojaView(CreateView):
    model = Loja
    template_name = "formulario_loja.html"
    form_class = LojaModelForm
    success_url = "/lojas/"


# Views baseadas em classes
class HomeView(TemplateView):
    template_name = 'home.html'


class ListarLojasView(ListView):
    model = Loja
    template_name = "lojas.html"
    context_object_name = "lojas"


class ListarBikesView(View):

    def get(self, request):
        bikes = Bike.objects.all()
        return render(request, "produtos.html", {"bikes": bikes})

    def post(): ...


class ListarBikesListView(ListView):
    model = Bike
    template_name = "produtos.html"
    context_object_name = "bikes"  # Interessante sempre informar o nome do contexto
    paginate_by = 10
    

    def get_queryset(self):
        return Bike.objects.order_by('preco')
    


class AtualizarLojaView(UpdateView):
    model = Loja
    template_name = "formulario_loja_update.html"
    form_class = LojaModelForm
    success_url = "/lojas/"


class DeletarLojaView(DeleteView):
    model = Loja
    template_name = "detalhe_loja.html"
    success_url = "/lojas/"


class DetalheLojaView(DetailView):
    model = Loja
    template_name = "detalhe_loja.html"
    # context_object_name = 'loja_de_bike'

class UpdateBikeView(UpdateView):
    model = Bike
    template_name = 'formulario_bike_update.html'
    form_class = BikeModelForm
    success_url = "/bikes/"

def cadastrar(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            bike_form = BikeModelForm(request.POST, request.FILES)
            if bike_form.is_valid(): 
                bike_form.save()
                return redirect("listar-bikes")
        else:
            bike_form = BikeModelForm()
        return render(request, 'formulario_bike.html', {'form': bike_form})
    else:
        return redirect("acessar")


# criar view para deletar aqui
def deletar_bike(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    bike.delete()
    return redirect("listar-bikes")





# Garantir que essa view retornar a lista de todos as bicicletas
def listar_bikes(request):

    bikes = Bike.objects.all() # -> Isso consulta no banco

    filtro =  request.GET.get('buscar') # pegar o filtro

    if filtro:
        bikes = bikes.filter(modelo__icontains=filtro) # Isso é uma consulta no banco de dados

    return render (request, 'produtos.html', {'bikes': bikes})


# def listar_lojas(request):
#     lojas = Loja.objects.all()
#     return render(request, 'lojas.html', {'lojas': lojas})


# def detalha_loja(request, id):
#     loja = get_object_or_404(Loja, pk=id)
#     return render(request, "detalhe_loja.html", {"loja": loja})


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

def atualizar_vendedor(request, pk):
    # Primeiro passo é pegar o vendedor
    vendedor = get_object_or_404(Vendedor, pk=pk)

    if request.method == 'POST':
        # No formulario passar os dados de POST e a instância do modelo
        form = VendedorModelForm(request.POST, instance=vendedor)
        if form.is_valid():
            form.save()
            return redirect("lista-vendedores")
    else:
        form = VendedorModelForm(instance=vendedor)
    return render(request, "formulario_atualizar_vendedor.html", {'form':form, "vendedor": vendedor})
