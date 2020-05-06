import discord
from discord.ext import commands
import time
import sys
import os
import json

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """
        Displays the average webstock latency.
        """

        x = self.bot.latency*1000
        ping = round(x)
        embed=discord.Embed(title="PING", color=0x36393e)
        embed.add_field(name=f"Average websocket latency", value=f"`Pong | {ping} ms`", inline=False)
        await ctx.send(embed=embed)



    # @commands.command()
    # async def help(self, ctx):
    #     embed=discord.Embed(title="HELP PANNEL", description=f"Your prefix: `$` || Mandatory :`<>` | Optional: `[]`\n\nType `$help [CategoryName]` to view more category information.\n", color=0x36393e)
    #     embed.add_field(name="__Info Category:__", value="`help`  `ping`", inline=False)
    #     embed.add_field(name="__Config Category:__", value="`setup`", inline=False)
    #     embed.add_field(name="__Ranking Category:__", value="`setrank`  `promote`  `demote`  `showrank`  `fire`", inline=False)
    #     embed.add_field(name="__Utility Category:__", value="`Ban`  `Unban`  `Mute`  `Unmute`  `kick` `purge`", inline=False)
    #     embed.add_field(name="__Owner Only:__", value="`load <cog>`  `unload <cog>`  `r`  `reload <cog>`", inline=False)
    #     await ctx.send(embed=embed)
    @commands.command()
    async def help(self, ctx):
        """
        Shows this message.
        """
        with open('data/help.json', 'r') as f:
            data = json.load(f)
        with open('data/help.json', 'w') as f:

            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    data[f"{filename[:-3]}"] = []
            json.dump(data, f, indent=4)
        # for i in self.bot.commands:

def setup(bot):
    bot.add_cog(Info(bot))
