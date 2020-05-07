import discord
from discord.ext import commands
import time
import sys
import os
import json

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Displays the average webstock latency.")
    async def ping(self, ctx):
        """
        Displays the average webstock latency.
        """

        x = self.bot.latency*1000
        ping = round(x)
        embed=discord.Embed(title="PING", color=0x36393e)
        embed.add_field(name=f"Average websocket latency", value=f"`Pong | {ping} ms`", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):

        embed=discord.Embed(title="Join our support server: http://support.rosystems.xyz/\nInvite RoSystems: http://invite.rosystems.xyz/", color=0x36393e)
        embed.set_author(name="RoSystems", icon_url="https://cdn.discordapp.com/attachments/700349605786943569/707905673777905724/transparent.png")

        await ctx.send(embed=embed)

    @commands.group(invoke_without_command=True, case_insensitive=True)
    async def help(self, ctx):
        embed=discord.Embed(title="HELP PANNEL", description=f"Your prefix: `$` || Mandatory :`<>` | Optional: `[]`\n\nType `$help [CategoryName]` to view more category information.\n", color=0x36393e)
        embed.add_field(name="__Info Category:__", value="`help`  `ping`", inline=False)
        embed.add_field(name="__Config Category:__", value="`setup`", inline=False)
        embed.add_field(name="__Ranking Category:__", value="`setrank`  `promote`  `demote`  `showrank`  `fire`", inline=False)
        embed.add_field(name="__Utility Category:__", value="`Ban`  `Unban`  `Mute`  `Unmute`  `kick`  `purge`", inline=False)
        embed.add_field(name="__Owner Only:__", value="`load <cog>`  `unload <cog>`  `r`  `reload <cog>`", inline=False)
        await ctx.send(embed=embed)

    @help.command(alias="info")
    async def Info(self, ctx):
        embed=discord.Embed(title="HELP PANNEL", description=f"Your prefix: `$` || Mandatory :`<>` | Optional: `[]`\n", color=0x36393e)
        embed.add_field(name="__Info Category:__", value="""`help [Category]` - Shows the help command.
          `ping` - Shows the average webstock latency.
          """, inline=False)
        await ctx.send(embed=embed)

    @help.command(alias="config")
    async def Config(self, ctx):
        embed=discord.Embed(title="HELP PANNEL", description=f"Your prefix: `$` || Mandatory :`<>` | Optional: `[]`\n", color=0x36393e)
        embed.add_field(name="__Config Category:__", value="""`setup` - Allows you to configure your server with RoSystems.
          """, inline=False)
        await ctx.send(embed=embed)

    @help.command(alias="ranking")
    async def Ranking(self, ctx):
        embed=discord.Embed(title="HELP PANNEL", description=f"Your prefix: `$` || Mandatory :`<>` | Optional: `[]`\n", color=0x36393e)
        embed.add_field(name="__Ranking Category:__", value="""`setrank <roblox-user> <rank-name>` - Changes the rank for a specific user.
        `promote <roblox-user>` - Promotes a user by one rank.
        `demote <roblox-user>` - Demotes a user by one rank.
        `showrank <roblox-user>` - Shows the rank for a specific user.
        `fire <roblox-user>` - Demotes a user to the lowest rank.
          """, inline=False)
        await ctx.send(embed=embed)

    @help.command(alias="utility")
    async def Utility(self, ctx):
        embed=discord.Embed(title="HELP PANNEL", description=f"Your prefix: `$` || Mandatory :`<>` | Optional: `[]`\n", color=0x36393e)
        embed.add_field(name="__Utility Category:__", value="""`ban <discord-user> [reason]` - Bans a user from the discord server.
        `Unban <discord-userID>` - Unbans a user from the discord server.
        `Mute <discord-user> <time (seconds)>` - Mutes a user for the specific time.
        `Unmute <discord-user>` - Unmutes the specified user.
        `Kick <discord-user> [reason]` -  Kicks a user from the discord server.
        `Purge <ammount> [target-discord-user]` - Purges the specified ammount of messages.
          """, inline=False)
        await ctx.send(embed=embed)












def setup(bot):
    bot.add_cog(Info(bot))
