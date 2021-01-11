from telethon import TelegramClient, events, sync

from config import *
from sql import *

client = TelegramClient('session_name', api_id, api_hash)
client.start()

sql = Sql(['id.db'])

print(client.get_me().stringify())

list_id = sql.get_users_id()

for id in list_id:
    try:
        client.send_message(id, 'Hello! Talking to you from Telethon and database')
    except:
        pass

client.download_profile_photo('me')
messages = client.get_messages('username')
messages[0].download_media()


@client.on(events.NewMessage(pattern='(?i)hi|hello'))
async def handler(event):
    await event.respond('Hey!')

client.run_until_disconnected()