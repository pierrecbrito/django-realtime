from django.shortcuts import render

def index(request):
    if request.method == "GET":
        return render(request, "identidade.html")
    elif request.method == "POST":
        nome = request.POST['nome']

        if nome: 
            ...
        else:
            return render(request, "identidade.html", {"mensagem": "Campo nome vazio ou inválido."})
