from discord.ext import commands
from echo_bot.constants import Responses
import random

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Hello")
    async def return_greeting(self, ctx):
        await ctx.send(random.choice(Responses.GREETINGS))