import os
from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from ponto.forms import FuncionarioForm, NewPontoForm, PontoSubmit
from ponto.models import Funcionario, Ponto
from django.utils import timezone
from django.contrib import messages

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    if request.method == 'POST':
        form = PontoSubmit(request.POST, request.FILES)
        if form.is_valid():
            
            data = Ponto.objects.last().dados

            for _ in range(10):
                data.readline()

            lines = data.readlines()
            
            data.close()

            pontos = []

            nome = form.cleaned_data['funcionario'].nome.split(' ')[0]
            mes = form.cleaned_data['mes']
            ano = form.cleaned_data['ano']

            for line in lines:
                line = line.decode('utf-8')
                if form.cleaned_data['funcionario'].pis in line:
                    pontos.append(
                        {
                            'data': line[10:12] + '/' + line[12:14] + '/' + line[14:18],
                            'hora': line[18:20] + ':' + line[20:22]
                        }
                    )

            resultado = []
            resultado_parcial = [pontos[0]['data']]
            data_atual = pontos[0]['data']
            
            for ponto in pontos:
                if ponto['data'][3:5] == mes and ponto['data'][6:10] == ano:
                    if ponto['data'][:2] != data_atual[:2]:
                        data_atual = ponto['data']
                        
                        if len(resultado_parcial) == 5:
                            total = timezone.datetime.strptime(resultado_parcial[4],'%H:%M') - timezone.datetime.strptime(resultado_parcial[1], '%H:%M') - (timezone.datetime.strptime(resultado_parcial[3], '%H:%M') - timezone.datetime.strptime(resultado_parcial[2], '%H:%M'))
                            resultado_parcial.append(str(total))                        
                        resultado.append(resultado_parcial)
                        resultado_parcial = [ponto['data']]
                    resultado_parcial.append(ponto['hora'])
            resultado = resultado[1:]
            
            for item in resultado:
                if len(item) < 6:
                    while(len(item) < 6): item.append("-")

            request.session['nome'] = nome
            request.session['resultado'] = resultado
            return redirect('resultados')

        else:
            messages.error(form.errors.as_data())
    
    form = PontoSubmit()
    funcionarios = Funcionario.objects.all().order_by('nome')
    ultimo_ponto = Ponto.objects.last()
    context = {
        'form': form,
        'funcionarios': funcionarios,
        'ultimo_ponto': ultimo_ponto,
    }
    return render(request, 'index.html', context)

@login_required(login_url='/accounts/login/')
def resultados(request):
    if request.session.get('resultado'):
        context = {
            'nome': request.session.get('nome'),
            'resultado': request.session.get('resultado')
        }
        return render(request, 'ponto/resultados.html', context)

@login_required(login_url='/accounts/login/')
def cadastrarFuncionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    form = FuncionarioForm()
    form.fields['pis'] = forms.CharField(max_length=12, min_length=12)
    context = {
        'form': form,
    }
    return render(request, 'ponto/funcionario_form.html', context)

@login_required(login_url='/accounts/login/')
def newPonto(request):
    if request.method == 'POST':
        form = NewPontoForm(request.POST, request.FILES)
        if form.is_valid():
            os.system('rm -rd media/')
            new_ponto = Ponto(dados=request.FILES['dados'], data=timezone.now())
            new_ponto.save()
            return redirect('index')
    ultimo_ponto = Ponto.objects.last()
    form = NewPontoForm()
    context = {
        'form': form,
        'ultimo_ponto': ultimo_ponto,
    }
    return render(request, 'ponto/ponto_form.html', context)