import discord
from discord.ext import commands
import time
import sys
import os
import requests
from bs4 import BeautifulSoup
import random
import asyncio

class Setup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def setup(self, ctx):
        def check(m):
            return m.author == ctx.author

        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value="Please ensure the bot has the correct permissions otherwise the setup will not work.", inline=False)
        await ctx.send(embed=embed)

        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value="What is your Roblox group ID?\n\n say **skip** to skip.\nsay **cancel** to cancel.", inline=False)
        embed.set_footer(text="This prompt will automatically cancel in 200 seconds.")
        await ctx.send(embed=embed)

        try:
            group_ID = await self.bot.wait_for('message', check=check, timeout=200)
        except asyncio.exceptions.TimeoutError:
            embed=discord.Embed(title="PROMPT TIMED OUT", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoServices.")
            await ctx.send(embed=embed)
            return

        if group_ID.content.upper() == 'SKIP':
            pass
        elif group_ID.content.upper() == 'CANCEL':
            embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoServices.")
            await ctx.send(embed=embed)
            return
        else:
            group_request = requests.get(url=f'https://groups.roblox.com/v1/groups/{int(group_ID.content)}/roles')
            roles = []
            for role in group_request.json().get('roles'):
                role.append(roles)
            await ctx.send(roles)
#https://www.roblox.com/users/{userId}/groups

def setup(bot):
    bot.add_cog(Setup(bot))
