from django import forms
from django.forms import formset_factory
from .models import Bike, Loja, Vendedor


class BikeModelForm(forms.ModelForm):

    class Meta:
        model = Bike
        fields = "__all__"

    def clean_preco(self):
        preco_cadastro = self.cleaned_data['preco']

        if preco_cadastro < 200:
            self.add_error('preco', 'O preço não pode ser menor do que R$200')

        return preco_cadastro

    def clean_foto(self):
        tamanho_maximo = 2

        imagem = self.cleaned_data.get('foto')

        # Converter a imagem
        tamanho_imagem = tamanho_maximo * 1024 * 1024

        # Validando o tamanho da imagem
        if imagem.size > tamanho_imagem:
            raise forms.ValidationError('A imagem tem um tamanho maior que o suportado')
        return imagem


class LojaModelForm(forms.ModelForm):
    class Meta:
        model = Loja
        fields = '__all__'


class VendedorModelForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = '__all__'







# Exemplo de uso de formulário personalizado
class ContactForm(forms.Form):
    template_name = "form_snippet.html"
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

# Usando multiplos formulário de uma unica vez
ContactFormSet = formset_factory(ContactForm, extra=2)

# class BikeForm(forms.Form):
#     modelo = forms.CharField(max_length=30)
#     preco = forms.FloatField(label='Preço')
#     descricao = forms.CharField(label='Descrição', widget=forms.Textarea)
#     foto = forms.ImageField()


#     def save(self):
#         bike = Bike(
#            modelo = self.cleaned_data['modelo'],
#            preco = self.cleaned_data['preco'],
#            descricao = self.cleaned_data['descricao'],
#            foto = self.cleaned_data['foto']
#         )

#         bike.save()

#         return bike
