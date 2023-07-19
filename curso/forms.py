from django.forms import ModelForm
from django import forms
from aluno.models import Curso

class CursoForm(ModelForm):

    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
        }