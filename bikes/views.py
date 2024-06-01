from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def produtos(request):
    return render(request, 'produtos.html')