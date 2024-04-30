# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from memory_profiler import profile


class ChatConsumer(AsyncWebsocketConsumer):
    @profile
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    @profile
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    @profile
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Create a struct of 1 Mb
        struct = bytearray(1024 * 1024)


        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

        # Send 1 Mb of data
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.binary", "message": struct}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))

    async def chat_binary(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(bytes_data=message)