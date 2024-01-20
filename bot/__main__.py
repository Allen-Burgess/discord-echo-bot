import os
import discord
from discord import Intents
from discord.message import Message

TOKEN = os.getenv("DISCORD_TOKEN")

intents = Intents.default()
intents.message_content = True
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    guild_count = 0

    for guild in client.guilds:
        print(f'- {guild.id}: {guild.name}')

        guild_count += 1

    print(f"Bot is connected to {guild_count} guilds")

client.run(TOKEN)