from django import forms
from django.utils import timezone
from ponto.models import Funcionario, Ponto
from ponto.validators import validate_month, validate_year

class PontoSubmit(forms.Form):
    funcionario = forms.ModelChoiceField(queryset=Funcionario.objects.all().order_by('nome'), label="Funcionário")
    
    mes_choices = []
    for i in range(12):
        if i < 9:
            mes_choices.append(('0'+str(i+1), '0'+str(i+1)))
        else:
            mes_choices.append((str(i+1), str(i+1)))

    ano_choices = []
    for i in range(timezone.now().year-1, timezone.now().year+1):
        ano_choices.append((str(i+1), str(i+1)))

    mes = forms.ChoiceField(label="Mês", choices=mes_choices)
    ano = forms.ChoiceField(choices=ano_choices)

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

class NewPontoForm(forms.ModelForm):
    class Meta:
        model = Ponto
        fields = ['dados']