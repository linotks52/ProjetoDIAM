# forms.py
from django import forms
from .models import Task, Utilizador


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'completed', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }




class UtilizadorForm(forms.ModelForm):
    imagem = forms.ImageField(required=False)
    class Meta:
        model = Utilizador
        fields = ['nome','email','descricao','imagem']

class UserForm(forms.ModelForm):
    class Meta:
        model = Utilizador
        exclude = ['datadecriacao']
        fields = ['nome', 'email', 'descricao','isAdmin', 'imagem', 'datadecriacao']
        widgets = {
            'datadecriacao': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'})
        }

