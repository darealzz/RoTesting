import discord
from discord.ext import commands
import time
import sys
import os
import requests
from bs4 import BeautifulSoup
import random
import asyncio
import robloxapi

# class Role:
#     """
#     Represents a role.
#     """
#     def __init__(self, role_id: int, role_name: str, rank: int, members: int):
#         """
#         :param role_id: The roles id
#         :param role_name: The roles name
#         :param rank: The roles rank (255, 254, etc)
#         :param members: How many users have the role
#         """
#         self.id = role_id
#         self.name = role_name
#         self.rank = rank
#         self.member_count = members

class Config(commands.Cog):
    #
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def setup(self, ctx):
        def check(m):
            return m.author == ctx.author
        def reactionCheck(reaction, user):
            if user == ctx.author and str(reaction.emoji) == '\U00000030\U0000fe0f\U000020e3':
                return True
            if user == ctx.author and str(reaction.emoji) == '\U00000031\U0000fe0f\U000020e3':
                return True
        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value="Please ensure the bot has the correct permissions otherwise the setup will not work.", inline=False)
        await ctx.send(embed=embed)

        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value="Please enter the token of the roblox?\n\nsay **cancel** to cancel.", inline=False)
        embed.set_footer(text="This prompt will automatically cancel in 200 seconds.")
        await ctx.send(embed=embed)

        try:
            token_cookie = await self.bot.wait_for('message', check=check, timeout=200)
        except asyncio.exceptions.TimeoutError:
            embed=discord.Embed(title="PROMPT TIMED OUT", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoServices.")
            await ctx.send(embed=embed)
            return

        if token_cookie.content.upper() == 'CANCEL':
            embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoServices.")
            await ctx.send(embed=embed)
            return
        else:
            try:
                client = robloxapi.Client(f'{token_cookie.content}')
                x=await client.get_self()
                await ctx.send(x.name, delete_after=1)
            except:
                embed=discord.Embed(title="AN INVALID TOKEN WAS GIVEN", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoServices.")
                await ctx.send(embed=embed)
                return
            # finally:
            #     await token_cookie.delete()
            #     await ctx.send(xtoken)
        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value=f"Please confirm that this is the correct account.\n`Account-name`: {x.name}\n`Account-ID`: {x.id}\n\nsay **cancel** to cancel.", inline=False)
        embed.set_footer(text="This prompt will automatically cancel in 200 seconds.")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('<:tick:700041815327506532>')
        await msg.add_reaction('<:rcross:700041862206980146>')
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=200, check=reactionCheck)
        except asyncio.exceptions.TimeoutError:
            embed=discord.Embed(title="PROMPT TIMED OUT", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoServices.")
            await ctx.send(embed=embed)
            return

        if token_cookie.content.upper() == 'CANCEL':
            embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoServices.")
            await ctx.send(embed=embed)
            return
        else:
            if str(reaction.emoji) == '<:tick:700041815327506532>':
                await ctx.send('message passed')
            elif str(reaction.emoji) == '<:rcross:700041862206980146>':
                await ctx.send('message returned')

def setup(bot):
    bot.add_cog(Config(bot))
