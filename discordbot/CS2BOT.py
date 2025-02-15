from typing import Final
import os
from responses import get_response, get_response_id
from discord import Intents, Client, Message
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")

# INTENTS
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


# MESSAGE
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('message empty no intent')
        return
    try:
        response: str = get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)
    try:
        response: int = get_response_id(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)


# 3 HANDLE RUN
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')


# 3 INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# MAIN
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
