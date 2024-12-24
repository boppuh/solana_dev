from utils.constants import TELEGRAM_API_ID, TELEGRAM_API_HASH

from telethon import TelegramClient


class TgClient:
    def __init__(self):
        self.client = TelegramClient('bot', TELEGRAM_API_ID, TELEGRAM_API_HASH)

    async def connect_client(self):
        await self.client.connect()

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
