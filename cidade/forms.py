from django.forms import ModelForm
from django import forms
from aluno.models import Cidade

class CidadeForm (ModelForm):

    class Meta:
        model = Cidade
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput (attrs={'class': 'form-control'}),
            'sigla_estado': forms.TextInput (attrs={'class': 'form-control'})
        }