from django.shortcuts import render, redirect

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
        return render(request, "chats.html")
 
