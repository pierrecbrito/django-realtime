from django.db import models

class Grupo(models.Model):
    nome = models.TextField(blank=False, max_length=400)
    
    def __str__(self):
        return f"{self.nome}"

class Mensagem(models.Model):
    nome_autor = models.TextField(blank=False, max_length=250)
    conteudo = models.TextField(blank=False, max_length=400)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    momento = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.nome_autor} diz que:  - {self.conteudo} -  em {self.grupo.nome} às {self.momento}"

