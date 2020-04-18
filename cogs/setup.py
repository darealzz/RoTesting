import discord
from discord.ext import commands
import time
import sys
import os
import requests
from bs4 import BeautifulSoup
import random
import asyncio

class Role:
    """
    Represents a role.
    """
    def __init__(self, role_id: int, role_name: str, rank: int, members: int):
        """
        :param role_id: The roles id
        :param role_name: The roles name
        :param rank: The roles rank (255, 254, etc)
        :param members: How many users have the role
        """
        self.id = role_id
        self.name = role_name
        self.rank = rank
        self.member_count = members

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
            return9
        else:
            try:
                r = requests.get(url=f'https://groups.roblox.com/v1/groups/{int(group_ID.content)}/roles')
            except ValueError:
                embed=discord.Embed(title="ENTER A VALID ID, PROMPT CANCELLED", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoServices.")
                await ctx.send(embed=embed)
                return
            #group = group_request.json()
            roles = []
            for role in r.json().get('roles'):
                roles.append(Role(role['id'], role['name'], role['rank'], role['memberCount']))
            new_roles = []
            for x in roles:
                new_roles.append(str(x.rank))
            new_roles = [int(x) for x in new_roles]
            new_roles.sort()

            discord_role = []
            async def disc_role_make():
                for role in r.json().get('roles'):
                    if role['rank'] == int(new_roles[0]):
                        await ctx.guild.create_role(name=role["name"])
                        new_roles.pop(0)
                #await ctx.send(sorted(group, key = lambda i: int(i['rank'])))


            #while len(new_roles) != 0:
                #await disc_role_make()


#https://www.roblox.com/users/{userId}/groups

def setup(bot):
    bot.add_cog(Setup(bot))
