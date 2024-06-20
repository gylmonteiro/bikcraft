from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Criar view para cadastrar usuario

def cadastrar_usuario(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('acessar')
    form = UserCreationForm()

    return render(request, 'cadastrar_usuario.html', {'form':form})

def acessar(request):
    
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # Ou retorna Nonese não tiver usuario,ou retorna o usuario

        if user:
            login(request, user)
            return redirect('pagina-inicial')

    
    form = AuthenticationForm()
    return render (request, 'acessar.html',  {'form': form})


def sair(request):
    logout(request)
    return redirect('pagina-inicial')