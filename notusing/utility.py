import discord
from discord.ext import commands
import time
import sys
import os
#0x36393e
class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(Utility(bot))
