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
        embed.add_field(name=f"Average websocket latency", value=f"`Pong | {ping} ms`", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="HELP PANNEL", description=f"Your prefix: `$` || Mandatory :`<>` | Optional: `[]`\n\nType `$help [CategoryName]` to view more category information.\n", color=0x36393e)
        embed.add_field(name="__Info Category:__", value="`help`  `ping`", inline=False)
        embed.add_field(name="__Config Category:__", value="`setup`", inline=False)
        embed.add_field(name="__Ranking Category:__", value="`setrank`  `promote`  `demote`  `showrank`  `fire`", inline=False)
        embed.add_field(name="__Moderation Category:__", value="`Ban`  `Unban`  `Mute`  `Unmute`  `kick` `purge`", inline=False)
        embed.add_field(name="__Owner Only:__", value="`load <cog>`  `unload <cog>`  `r`  `reload <cog>` `nuke`", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
