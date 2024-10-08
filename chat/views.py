from django.shortcuts import render, redirect
from .models import Grupo, Mensagem

def index(request):
    if request.method == "GET":
        if 'nome' not in request.session:
            return render(request, "identidade.html")
        else:
            return redirect('chats')
    elif request.method == "POST":
        nome = request.POST['nome']

        if nome: 
            request.session['nome'] = nome
            return redirect('chats')
        else:
            return render(request, "identidade.html", {"mensagem": "Campo nome vazio ou inválido."})

def chats(request):
    if request.method == "GET":
        if 'nome' in request.session:
            grupos = Grupo.objects.all()
            return render(request, "chats.html", {"grupos":grupos})
        else:
            return redirect('index')
        
def chat(request, grupo):
    if 'nome' in request.session:
        grupo = Grupo.objects.get(id=grupo)
        mensagens = Mensagem.objects.filter(grupo = grupo)
        return render(request, "chat.html", {"nome_grupo": grupo.nome, "mensagens": mensagens})
    return render(request, "identidade.html")

def logout(request):
    del request.session['nome']
    return redirect('index')

 
