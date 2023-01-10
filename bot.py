import discord
import responses

async def send_message(message, user_message,is_private):
    try:
        responses = responses.handle_response(user_message)
        await message.author.send(responses) if is_private else await message.channel.send(responses)
    except Exception as e:
        print(e)
        
def run_discord_bot():
    TOKEN = 'MTA2MjQxMzk3NjM4Nzk3NzMzNg.GMEBCa.RMGTOCechB0Kl1oeM3BD5PuPFvRyF8P44ciGu8'
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        
    
    client.run(TOKEN)