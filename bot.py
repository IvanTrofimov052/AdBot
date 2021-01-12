# ToDo: chats id

from telethon import TelegramClient, events, sync

from config import *
from sql import *

client = TelegramClient('session_name', api_id, api_hash)
client.start()

sql = Sql(['id.db'])

print(client.get_me().stringify())

list_id = sql.get_users_id()

@client.on(events.NewMessage(pattern=''))
async def handler(event):
    sender_id = str(event.sender_id)

    if sender_id == admin_id:
        for id in list_id:
            await client.send_message(id, event.text)


    await event.respond('Ok now it is working')

client.run_until_disconnected()