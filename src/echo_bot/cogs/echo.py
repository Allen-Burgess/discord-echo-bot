from discord.ext import commands

class Echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="echo")
    async def record_message(self, ctx, *args):
        await ctx.send(" ".join(args))