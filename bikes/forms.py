from django import forms
from .models import Bike

class BikeForm(forms.Form):
    modelo = forms.CharField(max_length=30)
    preco = forms.FloatField()
    descricao = forms.CharField(widget=forms.Textarea)
    foto = forms.ImageField()

    def save(self):
        bike = Bike(
           modelo = self.cleaned_data['modelo'],
           preco = self.cleaned_data['preco'],
           descricao = self.cleaned_data['descricao'],
           foto = self.cleaned_data['foto']
        )

        bike.save()

        return bike