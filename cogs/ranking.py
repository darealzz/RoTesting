import discord
from discord.ext import commands
import time
import sys
import os
import requests
import requests
from bs4 import BeautifulSoup
import json

class Ranking(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    async def configured(ctx):
        with open('data/groupdata.json', 'r') as f:
            data = json.load(f)
        if str(ctx.guild.id) in data:
            return True
        elif str(ctx.guild.id) not in data:
            await ctx.send('<:rcross:700041862206980146> You must configure your server with RoServices before using this command, use `setup`.')
            raise

    @commands.check(configured)
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def setrank(self, ctx, user=None, *, rank=None):
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
                embed.set_footer(text="All assets owned by RoServices")
                await ctx.send(embed=embed)
                return

            roles_request = requests.get(url=f'https://groups.roblox.com/v1/groups/{id}/roles')
            roles_json = roles_request.json()
            lst = []
            for role in roles_json.get('roles'):
                if role["name"] == rank:
                    lst.append(str(role["id"]))
            if len(lst) == 0:
                embed=discord.Embed(title="THIS RANK WAS NOT FOUND", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `help setup` for more information.", inline=False)
                embed.set_footer(text="All assets owned by RoServices")
                await ctx.send(embed=embed)
                return

            datax = {'roleId': str(lst[0])}
            cookie = {'.ROBLOSECURITY': str(cookie)}

            r = requests.post('https://www.roblox.com/favorite/toggle', cookies=cookie)
            await ctx.send(r.json())

            headers = {'X-CSRF-TOKEN': ''}
            user_request = requests.patch(url=f'https://groups.roblox.com/v1/groups/{id}/users/{user_Id}', headers=headers, cookies=cookie, data=datax)
            user_json = user_request.json()
            await ctx.send(user_json)

        if not rank:
            embed=discord.Embed(title="PLEASE PROVIDE ALL COMMAND AURGUMENTS", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `help setup` for more information.", inline=False)
            embed.set_footer(text="All assets owned by RoServices")
            await ctx.send(embed=embed)
            return
        if not user:
            embed=discord.Embed(title="PLEASE PROVIDE ALL COMMAND AURGUMENTS", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `help setup` for more information.", inline=False)
            embed.set_footer(text="All assets owned by RoServices")
            await ctx.send(embed=embed)
            return

def setup(bot):
    bot.add_cog(Ranking(bot))
