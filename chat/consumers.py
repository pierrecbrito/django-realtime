import json

from channels.generic.websocket import AsyncWebsocketConsumer

#Nós temos muitas instâncias do ChatConsumer
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.sala = self.scope['url_route']['kwargs']['grupo']
        self.sala_grupo = f'chat_{self.sala}'

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

        await self.channel_layer.group_send(
            self.sala_grupo,
            {
                'type': 'chat_mensagem',
                'mensagem': mensagem
            }
        )

    async def chat_mensagem(self, event):
        mensagem = event['mensagem']

        await self.send(text_data=json.dumps({
            'mensagem': mensagem
        }))