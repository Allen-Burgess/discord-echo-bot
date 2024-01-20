import os
from discord import Intents
from discord.ext import commands
from cogs import ALL_COGS

TOKEN = os.getenv("DISCORD_TOKEN")

intents = Intents.default()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix="!e ", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    guild_count = 0

    for guild in bot.guilds:
        print(f'- {guild.id}: {guild.name}')

        guild_count += 1

    print(f"Bot is connected to {guild_count} guilds")

    for cog in ALL_COGS:
        print(f"Adding cog: {str(cog)}")

    await bot.add_cog(cog(bot))

bot.run(TOKEN)