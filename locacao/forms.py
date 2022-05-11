from django import forms

from locacao.models import *


class LocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = ['cliente', 'carro', 'funcionaro', 'data_locacao', 'valor', 'data_devolucao']
