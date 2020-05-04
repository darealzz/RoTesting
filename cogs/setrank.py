import discord
from discord.ext import commands
import time
import sys
import os
import requests
import requests
from bs4 import BeautifulSoup
import json

class Setrank(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def setrank(self, ctx, user, rank=None):
        with open('data/groupdata.json') as f:
            data = json.load(f)
        if rank:
            cookie = data[f"{ctx.guild.id}"]["Cookie"]
            id = data[f"{ctx.guild.id}"]["ID"]

            user_request = requests.get(url=f'https://api.roblox.com/users/get-by-username?username={user}')
            user_json = user_request.json()
            try:
                user_name = user_json["Username"]
                user_Id = user_json["Id"]
            except KeyError:
                embed=discord.Embed(title="THIS USER DOES NOT EXIST", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `setrank` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoServices.")
                await ctx.send(embed=embed)
                return

            user_request = requests.patch(url=f'https://groups.roblox.com/v1/groups/{id}/users/{user_Id}')
            await ctx.send(f'Statuscode: {user_request}')
        if not rank:
            embed=discord.Embed(title="PLEASE PROVIDE ALL COMMAND AURGUMENTS", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `help setup` for more information.", inline=False)
            embed.set_footer(text="All assets owned by RoServices.")
            await ctx.send(embed=embed)
            return

def setup(bot):
    bot.add_cog(Setrank(bot))
