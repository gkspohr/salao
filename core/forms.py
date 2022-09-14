
from django import forms

class ClienteForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    sobrenome = forms.CharField(label='Sobrenome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    telefone = forms.CharField(label='Telefone', max_length=100)
    observacoes = forms.CharField(label='Observações', widget=forms.Textarea())
    # campos para CPF e endereço para puxar para nota fiscal

class FuncionarioForm(forms.Form):
    funcionario: forms.CharField(label='Nome Funcionario', max_length=30)
    sobrenome: forms.CharField(label='Sobrenome', max_length=100)
    cpf: forms.DecimalField(label='CPF', decimal_places=11)
    email: forms.EmailField(label='E-mail', max_length=100)
    telefone: forms.DecimalField(label='Telefone', decimal_places=11) 
    endereco: forms.CharField(label='Endereço', max_length=100)