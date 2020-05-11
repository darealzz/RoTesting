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
        except asyncio.exceptions.TimeoutError:
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
        embed = discord.Embed(title="PROMPT" ,description=f"Hello, {roblox_name.content}! To confirm that you own this Roblox account, please go here: https://www.roblox.com/my/account and put this code on your **profile or status**:", color=0x36393e)
        await ctx.send(embed=embed)
        embed = discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value=f"```{word_one} {word_two} {word_three} {word_four} {word_five}```\n\n say **done** when done.\nsay **cancel** to cancel.")
        embed.set_footer(text="This prompt will automatically cancel in 200 seconds.")
        await ctx.send(embed=embed)
        try:
            global wait_for_done
            wait_for_done = await self.bot.wait_for('message', check=check, timeout=200)
        except asyncio.exceptions.TimeoutError:
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




def setup(bot):
    bot.add_cog(UserAuth(bot))
