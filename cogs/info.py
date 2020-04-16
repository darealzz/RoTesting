import discord
from discord.ext import commands
import time
import sys
import os


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        x = self.bot.latency*1000
        ping = round(x)
        embed=discord.Embed(title="PING", color=0x36393e)
        embed.add_field(name=f"Average websocket latency", value=f"<:tick:700041815327506532> | `{ping} ms`", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
