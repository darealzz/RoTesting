import discord
from discord.ext import commands
import time
import sys
import os
#0x36393e
class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 644648271901622283 and message.content.upper=="HELP":
            await message.channel.send(f'{message.author.mention} **no i will not help u go learn python idiot**')

def setup(bot):
    bot.add_cog(Utility(bot))
