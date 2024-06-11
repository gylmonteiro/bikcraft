from django import forms
from .models import Bike


class BikeModelForm(forms.ModelForm):

    class Meta:
        model = Bike
        fields = "__all__"
    
    # Validação do preço
    def clean_preco(self):
        preco_cadastro = self.cleaned_data['preco']

        if preco_cadastro < 200:
            self.add_error('preco', 'O preço não pode ser menor do que R$200')
        
        return preco_cadastro
    

    # Validação do tamanho do arquivo de imagem
    def clean_foto(self):
        tamanho_maximo = 2

        imagem = self.cleaned_data.get('foto')

        # Converter a imagem
        tamanho_imagem = tamanho_maximo * 1024 * 1024


        # Validando o tamanho da imagem
        if imagem.size > tamanho_imagem:
            raise forms.ValidationError('A imagem tem um tamanho maior que o suportado')
        return imagem









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
