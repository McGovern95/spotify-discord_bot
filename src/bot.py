import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

client = discord.Client()

@client.event
async def on_ready():
    for server in client.guilds:
        if server.name == SERVER:
            break

    print(f'{client.user} has connected to Server: {server.name}\n')
    print('Peeps:\n {}'.format(' - '.join([member.name for member in server.members])))
    


client.run(TOKEN)