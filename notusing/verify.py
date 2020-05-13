import discord
from discord.ext import commands
import time
import sys
import json
import os
import robloxapi
import requests
from bs4 import BeautifulSoup
import random
import asyncio

# class Role:
#     def __init__(self, role_id: int, role_name: str, rank: int, members: int):
#
#         self.id = role_id
#         self.name = role_name
#         self.rank = rank
#         self.member_count = members
#
class UserAuth(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def in_guild(ctx):
        with open('cogs/guilds.json', 'r') as f:
            data = json.load(f)
        if str(ctx.guild.id) in data:
            return True
        elif str(ctx.guild.id) not in data:
            await ctx.send('<:rcross:700041862206980146> You must configure your server with RoServices before using this command, Use `setup`.')
            raise

    @commands.command()
    async def verify(self, ctx):

        def check(m):
            return m.author == ctx.author

        with open('data/users.json', 'r') as f:
            data = json.load(f)

        if str(ctx.author.id) in data:
            pass

        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value="What's your Roblox username?\n\nType **cancel** to cancel.", inline=False)
        embed.set_footer(text="This prompt will automatically cancel in 200 seconds.")
        await ctx.send(embed=embed)

        try:
            roblox_name = await self.bot.wait_for('message', check=check, timeout=200)
        except:
            embed=discord.Embed(title="PROMPT TIMED OUT", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `verify` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoServices.")
            await ctx.send(embed=embed)
            return

        if roblox_name.content.upper() == "CANCEL":
            embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `verify` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoServices.")
            await ctx.send(embed=embed)
            return

        response = requests.get(url=f"https://api.roblox.com/users/get-by-username?username={roblox_name.content}")
        json_r = response.json()
        try:
            userID = json_r['Id']
        except KeyError:
            embed=discord.Embed(title="ACCOUNT NOT FOUND, PROMPT CANCELLED.", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `verify` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoServices.")
            await ctx.send(embed=embed)
            return


        words = ['dog', 'car', 'oof', 'cat', 'bad', 'cool', 'fun', 'nice', 'play', 'roblox']

        word_one = random.choice(words)
        word_two = random.choice(words)
        word_three = random.choice(words)
        word_four = random.choice(words)
        word_five = random.choice(words)

        await ctx.send('https://cdn.discordapp.com/attachments/692517225558442065/696777741919584266/verify_help.png')

        embed = discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value=f"Hello, {roblox_name.content}! To confirm that you own this Roblox account, please go here: https://www.roblox.com/my/account and put this code on your **profile or status**:\n```{word_one} {word_two} {word_three} {word_four} {word_five}```\n\nsay **done** when done.\nsay **cancel** to cancel.")
        embed.set_footer(text="This prompt will automatically cancel in 200 seconds.")
        await ctx.send(embed=embed)
        try:
            global wait_for_done
            wait_for_done = await self.bot.wait_for('message', check=check, timeout=200)
        except:
            embed=discord.Embed(title="PROMPT TIMED OUT", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `verify` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoServices.")
            await ctx.send(embed=embed)
            return

        if wait_for_done.content.upper() == "DONE":
            pass
        elif wait_for_done.content.upper() == "CANCEL":
            embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `verify` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoServices.")
            await ctx.send(embed=embed)
            return
        elif wait_for_done.content.upper() not in ["DONE", "CANCEL"]:
            embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Please provide a valid response: `done` or `cancel`.", inline=False)
            embed.set_footer(text="All assets owned by RoServices.")
            await ctx.send(embed=embed)
            return

        blrub_request = requests.get(url=f'https://www.roblox.com/users/{int(userID)}/profile')
        soup = BeautifulSoup(blrub_request.text, "html.parser")
        try:
            blurb = soup.find('div', {'class': 'profile-about-content'}).pre.span.text
        except AttributeError:
            await ctx.send("<:rcross:700041862206980146> **We could not find the code on your profile, please restart the prompt and try again.**")
            return

        status_request = requests.get(url=f'https://www.roblox.com/users/profile/profileheader-json?userId={int(userID)}')
        status_json = status_request.json()
        status = status_json["UserStatus"]

        if blurb == f"{word_one} {word_two} {word_three} {word_four} {word_five}" or status == f"{word_one} {word_two} {word_three} {word_four} {word_five}":
            pass
        else:
            await ctx.send("<:rcross:700041862206980146> **We could not find the code on your profile, please restart the prompt and try again.**")
            return

        with open('data/users.json', 'r') as f:
            data = json.load(f)
        with open('data/users.json', 'w') as f:
            data[f"{ctx.author.id}"] = f"{roblox_name.content}"
            json.dump(data, f, indent=4)


        await ctx.send("<:tick:700041815327506532> **You have successfully been verified with RoServices!**")


#     @commands.command()
#     @commands.has_permissions(manage_guild=True)
#     async def setup(self, ctx):
#         def check(m):
#             return m.author == ctx.author
#
#         embed=discord.Embed(title="PROMPT", color=0x36393e)
#         embed.add_field(name="<:logo:700042045447864520>", value="Please ensure the bot has the correct permissions otherwise the setup will not work.", inline=False)
#         await ctx.send(embed=embed)
#
#         embed=discord.Embed(title="PROMPT", color=0x36393e)
#         embed.add_field(name="<:logo:700042045447864520>", value="What is your Roblox group ID?\n\n say **skip** to skip.\nsay **cancel** to cancel.", inline=False)
#         embed.set_footer(text="This prompt will automatically cancel in 200 seconds.")
#         await ctx.send(embed=embed)
#
#         try:
#             group_ID = await self.bot.wait_for('message', check=check, timeout=200)
#         except asyncio.exceptions.TimeoutError:
#             embed=discord.Embed(title="PROMPT TIMED OUT", color=0xee6551)
#             embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
#             embed.set_footer(text="All assets owned by RoServices.")
#             await ctx.send(embed=embed)
#             return
#
#         if group_ID.content.upper() == 'SKIP':
#             pass
#         elif group_ID.content.upper() == 'CANCEL':
#             embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
#             embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
#             embed.set_footer(text="All assets owned by RoServices.")
#             await ctx.send(embed=embed)
#             return
#         else:
#             try:
#                 r = requests.get(url=f'https://groups.roblox.com/v1/groups/{int(group_ID.content)}/roles')
#             except ValueError:
#                 embed=discord.Embed(title="ENTER A VALID ID, PROMPT CANCELLED", color=0xee6551)
#                 embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
#                 embed.set_footer(text="All assets owned by RoServices.")
#                 await ctx.send(embed=embed)
#                 return
#             #group = group_request.json()
#             roles = []
#             for role in r.json().get('roles'):
#                 roles.append(Role(role['id'], role['name'], role['rank'], role['memberCount']))
#             new_roles = []
#             for x in roles:
#                 new_roles.append(str(x.rank))
#             new_roles = [int(x) for x in new_roles]
#             new_roles.sort()
#
#             discord_role = []
#             async def disc_role_make():
#                 for role in r.json().get('roles'):
#                     if role['rank'] == int(new_roles[0]):
#                         await ctx.guild.create_role(name=role["name"])
#                         new_roles.pop(0)
#                 #await ctx.send(sorted(group, key = lambda i: int(i['rank'])))
#
#
#         embed=discord.Embed(title="PROMPT", color=0x36393e)
#         embed.add_field(name="<:logo:700042045447864520>", value="""
# ```
# {discord-name} --> changes to their Discord username
# {roblox-id} --> changes to their ROBLOX ID
# {roblox-name} --> changes to their ROBLOX Username
# {group-rank} --> changes to their current rank in the linked group
# Note: the {} must be included in the template```Enter the nickname layout you want for your server.\n\n say **skip** to skip.\nsay **cancel** to cancel.""", inline=False)
#         embed.set_footer(text="This prompt will automatically cancel in 200 seconds.")
#         await ctx.send(embed=embed)
#
#         try:
#             nickname_layout = await self.bot.wait_for('message', check=check, timeout=200)
#         except asyncio.exceptions.TimeoutError:
#             embed=discord.Embed(title="PROMPT TIMED OUT", color=0xee6551)
#             embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
#             embed.set_footer(text="All assets owned by RoServices.")
#             await ctx.send(embed=embed)
#             return
#
#         if nickname_layout.content.upper() == 'SKIP':
#             pass
#         elif nickname_layout.content.upper() == 'CANCEL':
#             embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
#             embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
#             embed.set_footer(text="All assets owned by RoServices.")
#             await ctx.send(embed=embed)
#             return
#         else:
#             words = nickname_layout.content.split()
#             for i in words:
#                 if i not in ['{discord-name}', '{roblox-id}', '{roblox-name}', '{group-rank}']:
#                     embed=discord.Embed(title="INVALID FORMAT/VALUES, PROMPT CANCELLED", color=0xee6551)
#                     embed.add_field(name="<:logo:700042045447864520>", value="Type `setup` to restart prompt.", inline=False)
#                     embed.set_footer(text="All assets owned by RoServices.")
#                     await ctx.send(embed=embed)
#                     break
#                     return
#
#
#
#             #while len(new_roles) != 0:
#                 #await disc_role_make()


def setup(bot):
    bot.add_cog(UserAuth(bot))
