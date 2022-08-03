from django.urls import path
from ponto import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar', views.cadastrarFuncionario, name='cadastrar'),
    path('resultados', views.resultados, name='resultados'),
    path('ponto', views.newPonto, name='newPonto'),
]