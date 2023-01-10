# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTA2MjQxMzk3NjM4Nzk3NzMzNg.GMEBCa.RMGTOCechB0Kl1oeM3BD5PuPFvRyF8P44ciGu8')
