import discord
from discord.ext import commands
import time
import sys
import os
import asyncio
import random
from discord.utils import get
class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # @comands.command()
    # async def on


def setup(bot):
    bot.add_cog(Utility(bot))
