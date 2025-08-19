import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import VideoRoom


class VideoCallConsumer(AsyncWebsocketConsumer):
    # Вызывается, когда React пытается подключиться по WebSocket
    async def connect(self):
        # 1. Получаем ID комнаты из URL, например: /ws/videocall/abc-123-def/
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'videocall_{self.room_id}'

        # 2. Проверяем в базе данных, существует ли такая комната
        if not await self.room_exists(self.room_id):
            # Если комнаты нет, молча закрываем соединение.
            await self.close()
            return

        # 3. Если комната существует, "присоединяем" этого пользователя
        # к общей группе рассылки для этой комнаты.
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # 4. Сообщаем React'у, что соединение успешно установлено.
        await self.accept()

    # Вызывается, когда пользователь закрывает вкладку или уходит со страницы
    async def disconnect(self, close_code):
        # Удаляем пользователя из группы рассылки
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Вызывается, когда с React'a приходит какое-либо сообщение
    async def receive(self, text_data):
        # Просто пересылаем это сообщение всем остальным участникам комнаты
        # Это и есть наша "сигнализация" для WebRTC.
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'videocall_message',  # Эта строка говорит, какой метод-обработчик вызвать
                'message': text_data
            }
        )

    # Метод-обработчик, который вызывается командой `group_send`
    async def videocall_message(self, event):
        message = event['message']
        # Отправляем полученное сообщение обратно в React
        await self.send(text_data=message)

    # Специальная функция, которая позволяет безопасно обращаться к
    # синхронной базе данных Django из асинхронного кода
    @database_sync_to_async
    def room_exists(self, room_id):
        return VideoRoom.objects.filter(id=room_id).exists()