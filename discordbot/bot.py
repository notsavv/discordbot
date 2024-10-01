import discord
import requests


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('hello'):
            print('message detected')
            await message.channel.send('Hello World!')

intents: Intents = Intents.default()
intents.message_content = True
client: Client = MyClient(intents=intents)


client.run('MTI5MDU0ODYzNDY1MTQ2MzcyMA.GkDZLy.Ot2OO6-x5VmVnwEiG6J3nSwEZ8ym1DJ2w4Y5dY')  # Replace with your own .env.
