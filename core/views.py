from django.shortcuts import render


from .forms import ClienteForm, FuncionarioForm

def index(request):
    return render(request, 'index/index.html')

def login(request):
    return render(request, 'login/login.html')    

def agenda(request):
    return render(request, 'agenda.html')    

def cliente(request):
    form = ClienteForm()
    return render(request, 'cliente.html') 

def funcionario(request):
    form = FuncionarioForm()
    return render(request, 'funcionario.html')

def listaprecos(request):
    return render(request, 'listaprecos.html')

def register(request):
    return render(request, 'login/register.html')    