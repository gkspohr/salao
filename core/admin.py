from django.contrib import admin

from .models import Agenda, Cliente, Funcionario
from .forms import ClienteForm, FuncionarioForm


#class ClienteAdmin(admin.ModelAdmin):
#    list_display = ('Nome',)

#class FuncionarioAdmin(admin.ModelAdmin):
#    list_display = ('Nome', 'Sobrenome', 'CPF', 'E-mail', 'Telefone', 'Endereço')


#admin.site.register(Agenda)

admin.site.register(Cliente)

#admin.site.register(Funcionario, FuncionarioAdmin),