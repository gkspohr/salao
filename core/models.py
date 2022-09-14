from tkinter import CASCADE
from django.db import models

from core.views import funcionario, agenda, cliente

class Funcionario(models.Model):
    funcionario= models.CharField('Nome Funcionario', null=True, blank=True, max_length=30)
    sobrenome= models.CharField('Sobrenome', null=True, blank=True, max_length=100)
    cpf= models.DecimalField('CPF', null=True, blank=True, decimal_places=11, max_digits=11)
    email= models.EmailField('E-mail', null=True, blank=True, max_length=100)
    telefone= models.DecimalField('Telefone', null=True, blank=True, decimal_places=11, max_digits=11) 
    endereco= models.CharField('Endereço', null=True, blank=True, max_length=100)   


class Agenda(models.Model):
    funcionario= models.ForeignKey(Funcionario, null=True, blank=True , on_delete=models.PROTECT, max_length=100) 
    dia= models.DateTimeField('Dia e Horario', null=True, blank=True, max_length=100)
    # status pesquisar campo choise para escolher Funcionarios
    

class Cliente(models.Model):
    nome = models.CharField('Nome', null=True, blank=True, max_length=30)
    sobrenome = models.CharField('Sobrenome', null=True, blank=True, max_length=100)
    email = models.EmailField('E-mail', null=True, blank=True, max_length=100)
    telefone = models.CharField('Telefone',null=True, blank=True, max_length=20) 
    # existe campo phonenumber - estudar

    def __str__(self):
        return self.nome

 