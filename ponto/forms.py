from django import forms
from django.utils import timezone
from ponto.models import Funcionario, Ponto

class PontoSubmit(forms.Form):
    funcionario = forms.ModelChoiceField(
        queryset=Funcionario.objects.all().order_by('nome'), 
        label="Funcionário",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    mes_choices = []
    for i in range(12):
        if i < 9:
            mes_choices.append(('0'+str(i+1), '0'+str(i+1)))
        else:
            mes_choices.append((str(i+1), str(i+1)))

    ano_choices = []
    for i in range(timezone.now().year-1, timezone.now().year+1):
        ano_choices.append((str(i+1), str(i+1)))

    mes = forms.ChoiceField(
        label="Mês", 
        choices=mes_choices,
        widget=forms.Select(attrs={'class': 'form-select w-25'})
    )
    ano = forms.ChoiceField(choices=ano_choices, widget=forms.Select(attrs={'class': 'form-select w-25'}))

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'pis': forms.TextInput(attrs={'class': 'form-control w-50', 'min': '12', 'max':'12'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control w-25'}),
            'entrada': forms.Select(attrs={'class': 'form-select w-25'}),
            'almoco': forms.Select(attrs={'class': 'form-select w-25'}),
            
        }

class NewPontoForm(forms.ModelForm):
    class Meta:
        model = Ponto
        fields = ['dados']
        widgets = {
            'dados': forms.FileInput(attrs={'class': 'form-control'})
        }