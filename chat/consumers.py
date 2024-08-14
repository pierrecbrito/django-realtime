import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Mensagem, Grupo
from datetime import timedelta

#Nós temos muitas instâncias do ChatConsumer
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.sala = self.scope['url_route']['kwargs']['grupo']
        self.sala_grupo = f'chat_{self.sala}'
        self.grupo = await self.get_grupo(self.sala)

        await self.channel_layer.group_add(
            self.sala_grupo,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.sala_grupo,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        mensagem = text_data_json['mensagem']
        remetente = text_data_json['remetente']

        nova_mensagem = await self.save_mensagem(remetente=remetente, mensagem=mensagem, grupo=self.grupo)

        nova_mensagem.momento = nova_mensagem.momento - timedelta(hours=3, minutes=0)
        await self.channel_layer.group_send(
            self.sala_grupo,
            {
                'type': 'chat_mensagem',
                'mensagem': mensagem,
                'remetente': remetente,
                'momento': nova_mensagem.momento.strftime("%d/%m/%Y %H:%M") + "h"
            }
        )

    async def chat_mensagem(self, event):
        mensagem = event['mensagem']
        remetente = event['remetente']
        momento = event['momento']

        await self.send(text_data=json.dumps({
            'mensagem': mensagem,
            'remetente': remetente,
            'momento': momento
        }))

    @database_sync_to_async
    def get_grupo(self, grupo_nome):
        return Grupo.objects.get(nome=grupo_nome)
    
    @database_sync_to_async
    def save_mensagem(self, remetente, mensagem, grupo):
        nova_mensagem = Mensagem(nome_autor=remetente, conteudo=mensagem, grupo=grupo)
        nova_mensagem.save()
        return nova_mensagem