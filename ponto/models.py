from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    pis = models.CharField(max_length=12, verbose_name="PIS")
    matricula = models.CharField(max_length=5, verbose_name="Matrícula")
    entrada_choices = (
        ("7", "7:00"),
        ("8", "8:00")
    )
    entrada = models.CharField(max_length=1, choices=entrada_choices)
    
    almoco_choices = (
        ("11", "11:00"),
        ("12", "12:00"),
        ("13", "13:00")
    )
    almoco = models.CharField(max_length=2, choices=almoco_choices, verbose_name="Almoço")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Funcionário"

class Ponto(models.Model):
    data = models.DateTimeField()
    dados = models.FileField(upload_to="media/")