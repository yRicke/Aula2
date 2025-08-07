from django.shortcuts import render, redirect
from agenda.models import Agenda

# Create your views here.

def novo_contato(request):
    if request.method =='POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        Agenda.novo(nome, telefone)
        return render(request, 'add_contato.html')
    return render(request, 'add_contato.html')

def listar_contatos(request):
    contatos = Agenda.listar()
    return render(request, 'index.html', {'contatos': contatos})

def apagar_contato(request, id):
    Agenda.deletar(id)
    return redirect('listar_contatos')