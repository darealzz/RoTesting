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
import json
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
            if user == ctx.author and reaction.emoji == tick:
                return True
            if user == ctx.author and reaction.emoji == cross:
                return True
        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value="Please ensure the bot has the correct permissions otherwise the setup will not work.", inline=False)
        await ctx.send(embed=embed)

        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value="What is the ROBLOX account token?\n\nsay **cancel** to cancel.", inline=False)
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
                await ctx.send(x.name, delete_after=0.1)
                lst=[]
                lst.append(f'{token_cookie.content}')
            except:
                embed=discord.Embed(title="AN INVALID TOKEN WAS GIVEN", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoServices.")
                await ctx.send(embed=embed)
                return
        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value=f"Please confirm that this is the correct account.\n`Account-name`: {x.name}\n`Account-ID`: {x.id}\n\nsay **cancel** to cancel.", inline=False)
        embed.set_footer(text="This prompt will automatically cancel in 200 seconds.")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('<:tick:700041815327506532>')
        await msg.add_reaction('<:rcross:700041862206980146>')
        tick = self.bot.get_emoji(700041815327506532)
        cross = self.bot.get_emoji(700041862206980146)
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
            if reaction.emoji == tick:
                await token_cookie.delete()
                pass
            elif reaction.emoji == cross:
                await token_cookie.delete()
                embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoServices.")
                await ctx.send(embed=embed)
                return


        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value="What is the your ROBLOX group ID?\n\nsay **cancel** to cancel.", inline=False)
        embed.set_footer(text="This prompt will automatically cancel in 200 seconds.")
        await ctx.send(embed=embed)

        try:
            groupID = await self.bot.wait_for('message', check=check, timeout=200)
        except asyncio.exceptions.TimeoutError:
            embed=discord.Embed(title="PROMPT TIMED OUT", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoServices.")
            await ctx.send(embed=embed)
            return

        if groupID.content.upper() == 'CANCEL':
            embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoServices.")
            await ctx.send(embed=embed)
            return
        else:
            try:
                groupID_request = requests.get(url=f'https://groups.roblox.com/v1/groups/{int(groupID.content)}/')
                groupID_json = groupID_request.json()
                groupID_name = groupID_json["name"]
                groupID_id = groupID_json["id"]
                groupID_memberCount = groupID_json["memberCount"]
                groupID_owner = groupID_json["owner"]["username"]
                groupID_ownerID = groupID_json["owner"]["userId"]
            except KeyError:
                embed=discord.Embed(title="GROUP DOES NOT EXIST, PROMPT CANCELLED", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoServices.")
                await ctx.send(embed=embed)
                return

            groupUsers_request = requests.get(url=f"https://groups.roblox.com/v1/groups/{int(groupID_id)}/users/{int(x.id)}")
            await ctx.send(groupUsers_request)


    # @commands.command()
    # async def x(self, ctx):
    #     with open('cogs/tester.json', 'r') as f:
    #         json.load(f)
    #     with open('cogs/tester.json', 'w') as f:
    #         data = {"previousPageCursor":"null","nextPageCursor":"2_1_d09dc216063e729176e256f6fa903dd5","data":[{"user":{"buildersClubMembershipType":"None","userId":116593815,"username":"lordDragonmaster112","displayName":"lordDragonmaster112+DN"},"role":{"id":34266627,"name":"[8] Head of Security","rank":9,"memberCount":1}},{"user":{"buildersClubMembershipType":"None","userId":185635988,"username":"The_Fortaken","displayName":"The_Fortaken+DN"},"role":{"id":34123143,"name":"[5] Security","rank":6,"memberCount":1}},{"user":{"buildersClubMembershipType":"None","userId":573280920,"username":"mightyduck123445","displayName":"mightyduck123445+DN"},"role":{"id":34266639,"name":"[1] Resort Guest","rank":1,"memberCount":82}},{"user":{"buildersClubMembershipType":"None","userId":1159486467,"username":"Hockey3566","displayName":"Hockey3566+DN"},"role":{"id":34266639,"name":"[1] Resort Guest","rank":1,"memberCount":82}},{"user":{"buildersClubMembershipType":"None","userId":114047853,"username":"IamSidzilla","displayName":"IamSidzilla+DN"},"role":{"id":34266639,"name":"[1] Resort Guest","rank":1,"memberCount":82}},{"user":{"buildersClubMembershipType":"None","userId":513129713,"username":"DeputyBlue","displayName":"DeputyBlue+DN"},"role":{"id":34266639,"name":"[1] Resort Guest","rank":1,"memberCount":82}},{"user":{"buildersClubMembershipType":"None","userId":266397796,"username":"littletucktuck","displayName":"littletucktuck+DN"},"role":{"id":34266639,"name":"[1] Resort Guest","rank":1,"memberCount":82}},{"user":{"buildersClubMembershipType":"None","userId":629086208,"username":"pepeandrem032008","displayName":"pepeandrem032008+DN"},"role":{"id":34123069,"name":"[10] Manager","rank":14,"memberCount":1}},{"user":{"buildersClubMembershipType":"None","userId":1242302230,"username":"Cute_GalaxyWolf235","displayName":"Cute_GalaxyWolf235+DN"},"role":{"id":34266639,"name":"[1] Resort Guest","rank":1,"memberCount":82}},{"user":{"buildersClubMembershipType":"None","userId":1258233717,"username":"pariona100300p","displayName":"pariona100300p+DN"},"role":{"id":34266639,"name":"[1] Resort Guest","rank":1,"memberCount":82}}]}
    #         json.dump(data, f, indent=5)

def setup(bot):
    bot.add_cog(Config(bot))
