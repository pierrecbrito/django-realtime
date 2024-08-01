from django.shortcuts import render, redirect

def index(request):
    if request.method == "GET":
        return render(request, "identidade.html")
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
 
