from utils.constants import TELEGRAM_API_ID, TELEGRAM_API_HASH

from telethon import TelegramClient, events
import logging


class TgClient:
    def __init__(self, message_handler=None):
        self.client = TelegramClient('bot', TELEGRAM_API_ID, TELEGRAM_API_HASH)
        self.message_handler = message_handler

    async def connect_client(self):
        await self.client.start(phone='+15047236957')
        await self.register_events()

    async def register_events(self):
        @self.client.on(events.NewMessage)  # NewMessage(chats=channels)
        async def handler(event):
            try:
                message_content = event.message.message if event.message else ""
                if self.message_handler:
                    self.message_handler.handle_new_message(message_content)

            except Exception as e:
                print(e)

        await self.client.run_until_disconnected()

    async def channels_to_filter(self):
        channel_names = ['CryptoBoltzSquad', 'trending', 'MAXBIDDERSTRENCHES']
        channels = []
        for channel_name in channel_names:
            entity = await self.get_entity(channel_name)
            if entity:
                channels.append(entity)
        return channels

    async def send_message(self, entity_name, message):
        entity = await self.get_entity(entity_name)
        if entity:
            await self.client.send_message(entity, message)
        else:
            print(f"Entity {entity_name} not found")

    async def get_entity(self, entity_name):
        try:
            entity = await self.client.get_entity(entity_name)
            return entity
        except Exception as e:
            return None

    async def scrape_messages(self, entity_name, limit=100):
        entity = await self.get_entity(entity_name)
        messages = []
        async for message in self.client.iter_messages(entity, limit=limit):
            messages.append({
                'id': message.id,
                'date': message.date.strftime('%Y-%m-%d %H:%M:%S'),
                'text': message.text
            })
        return messages
