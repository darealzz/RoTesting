import discord
from discord.ext import commands
import time
import sys
import os
import requests
import requests
from bs4 import BeautifulSoup
import json
import robloxapi

class Roblox(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    async def configured(ctx):
        with open('data/groupdata.json', 'r') as f:
            data = json.load(f)
        if str(ctx.guild.id) in data:
            cookie = data[f"{ctx.guild.id}"]["Cookie"]
            group = await client.get_group(id)
            client = robloxapi.client(cookie)
            await client.get_self()
            return True
        elif str(ctx.guild.id) not in data:
            await ctx.send('<:rcross:700041862206980146> You must configure your server with RoSystems before using this command, use `setup`.')
            raise discord.ext.commands.CommandNotFound


    @commands.has_permissions(manage_guild=True)
    @commands.check(configured)
    @commands.command()
    async def setrank(self, ctx, user, *, rank):
        """
        Sets the rank for a specific user to a specific rank.
        """
        def reactionCheck(reaction, user):
            if user == ctx.author and reaction.emoji == tick:
                return True
            if user == ctx.author and reaction.emoji == cross:
                return True
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
                embed.set_footer(text="All assets owned by RoSystems")
                await ctx.send(embed=embed)
                return

            roles_request = requests.get(url=f'https://groups.roblox.com/v1/groups/{id}/roles')
            roles_json = roles_request.json()
            lst = []
            for role in roles_json.get('roles'):
                if role["name"] == rank:
                    lst.append(str(role["id"]))
                    lst.append(str(role["name"]))
            if len(lst) == 0:
                embed=discord.Embed(title="THIS RANK WAS NOT FOUND", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `help ranking` for more information.", inline=False)
                embed.set_footer(text="All assets owned by RoSystems")
                await ctx.send(embed=embed)
                return

            client = robloxapi.Client(cookie)
            RobloxUser_object = await client.get_user(name=f"{user_name}")
            try:
                x = await RobloxUser_object.get_role_in_group(id)
            except robloxapi.utils.errors.NotFound:
                embed=discord.Embed(title="THIS USER IS NOT IN THE GROUP, PROMPT CANCELLED", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `setrank` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoSystems")
                await ctx.send(embed=embed)
                return

            embed=discord.Embed(title="PROMPT", color=0x36393e)
            embed.add_field(name="<:logo:700042045447864520>", value=f"Please confirm that this is the correct data.\n`Account-name`: {user_name}\n`Account-ID`: {user_Id}\n`Currant-rank`: {x.name}\n`New-rank`: {lst[1]}\n\nsay **cancel** to cancel.", inline=False)
            embed.set_footer(text="This prompt will automatically cancel in 200 seconds.")
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('<:tick:700041815327506532>')
            await msg.add_reaction('<:rcross:700041862206980146>')
            tick = self.bot.get_emoji(700041815327506532)
            cross = self.bot.get_emoji(700041862206980146)
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=200, check=reactionCheck)
            except:
                embed=discord.Embed(title="PROMPT TIMED OUT", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `setrank` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoSystems")
                await ctx.send(embed=embed)
                return
            else:
                if reaction.emoji == tick:
                    pass
                elif reaction.emoji == cross:
                    embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
                    embed.add_field(name="<:logo:700042045447864520>", value="Type `setrank` to restart prompt.", inline=False)
                    embed.set_footer(text="All assets owned by RoSystems")
                    await ctx.send(embed=embed)
                    return


                group = await client.get_group(id)
                try:
                    await group.set_rank(user_Id, int(lst[0]))
                except robloxapi.utils.errors.BadStatus:
                    embed=discord.Embed(title="YOU CANNOT CHANGE THIS ACCOUNTS RANK, PROMPT CANCELLED", color=0xee6551)
                    embed.add_field(name="<:logo:700042045447864520>", value="Type `setrank` to restart prompt.", inline=False)
                    embed.set_footer(text="All assets owned by RoSystems")
                    await ctx.send(embed=embed)
                    return

                embed=discord.Embed(title="USER WAS SUCCESSFULLY RANKED", color=0x1de97b)
                embed.set_footer(text="All assets owned by RoSystems")
                await ctx.send(embed=embed)
                return


    @commands.has_permissions(manage_guild=True)
    @commands.check(configured)
    @commands.command()
    async def promote(self, ctx, user):
        """
        Promotes a user by one rank.
        """
        def reactionCheck(reaction, user):
            if user == ctx.author and reaction.emoji == tick:
                return True
            if user == ctx.author and reaction.emoji == cross:
                return True
        with open('data/groupdata.json') as f:
            data = json.load(f)
        cookie = data[f"{ctx.guild.id}"]["Cookie"]
        id = data[f"{ctx.guild.id}"]["ID"]
        user_request = requests.get(url=f'https://api.roblox.com/users/get-by-username?username={user}')
        user_json = user_request.json()

        try:
            user_name = user_json["Username"]
            user_Id = user_json["Id"]
        except KeyError:
            embed=discord.Embed(title="THIS USER DOES NOT EXIST", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `promote` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        client = robloxapi.Client(cookie)
        RobloxUser_object = await client.get_user(name=f"{user_name}")
        try:
            x = await RobloxUser_object.get_role_in_group(id)
        except robloxapi.utils.errors.NotFound:
            embed=discord.Embed(title="THIS USER IS NOT IN THE GROUP, PROMPT CANCELLED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `promote` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        roles_request = requests.get(url=f'https://groups.roblox.com/v1/groups/{id}/roles')
        roles_json = roles_request.json()
        lst = []
        for role in roles_json.get('roles'):
            if role["name"] == x.name:
                ransk = x.rank + 1
        for role in roles_json.get('roles'):
            if role["rank"] == ransk:
                new = role["name"]



        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value=f"Please confirm that this is the correct data.\n`Account-name`: {user_name}\n`Account-ID`: {user_Id}\n`Currant-rank`: {x.name}\n`New-rank`: {new}\n\nsay **cancel** to cancel.", inline=False)
        embed.set_footer(text="This prompt will automatically cancel in 200 seconds.")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('<:tick:700041815327506532>')
        await msg.add_reaction('<:rcross:700041862206980146>')
        tick = self.bot.get_emoji(700041815327506532)
        cross = self.bot.get_emoji(700041862206980146)
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=200, check=reactionCheck)
        except:
            embed=discord.Embed(title="PROMPT TIMED OUT", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `promote` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        else:
            if reaction.emoji == tick:
                pass
            elif reaction.emoji == cross:
                embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `promote` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoSystems")
                await ctx.send(embed=embed)
                return


            group = await client.get_group(id)
            try:
                await group.promote(user_Id)
            except robloxapi.utils.errors.BadStatus:
                embed=discord.Embed(title="YOU CANNOT CHANGE THIS ACCOUNTS RANK, PROMPT CANCELLED", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `promote` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoSystems")
                await ctx.send(embed=embed)
                return

            embed=discord.Embed(title="USER WAS SUCCESSFULLY PROMOTED", color=0x1de97b)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)

    @commands.has_permissions(manage_guild=True)
    @commands.check(configured)
    @commands.command()
    async def demote(self, ctx, user):
        """
        Demotes a user by one rank.
        """

        def reactionCheck(reaction, user):
            if user == ctx.author and reaction.emoji == tick:
                return True
            if user == ctx.author and reaction.emoji == cross:
                return True
        with open('data/groupdata.json') as f:
            data = json.load(f)
        cookie = data[f"{ctx.guild.id}"]["Cookie"]
        id = data[f"{ctx.guild.id}"]["ID"]
        user_request = requests.get(url=f'https://api.roblox.com/users/get-by-username?username={user}')
        user_json = user_request.json()

        try:
            user_name = user_json["Username"]
            user_Id = user_json["Id"]
        except KeyError:
            embed=discord.Embed(title="THIS USER DOES NOT EXIST", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `demote` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        client = robloxapi.Client(cookie)
        RobloxUser_object = await client.get_user(name=f"{user_name}")
        try:
            x = await RobloxUser_object.get_role_in_group(id)
        except robloxapi.utils.errors.NotFound:
            embed=discord.Embed(title="THIS USER IS NOT IN THE GROUP, PROMPT CANCELLED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `demote` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        roles_request = requests.get(url=f'https://groups.roblox.com/v1/groups/{id}/roles')
        roles_json = roles_request.json()
        lst = []
        for role in roles_json.get('roles'):
            if role["name"] == x.name:
                ransk = x.rank - 1
        for role in roles_json.get('roles'):
            if role["rank"] == ransk:
                new = role["name"]



        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value=f"Please confirm that this is the correct data.\n`Account-name`: {user_name}\n`Account-ID`: {user_Id}\n`Currant-rank`: {x.name}\n`New-rank`: {new}\n\nsay **cancel** to cancel.", inline=False)
        embed.set_footer(text="This prompt will automatically cancel in 200 seconds.")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('<:tick:700041815327506532>')
        await msg.add_reaction('<:rcross:700041862206980146>')
        tick = self.bot.get_emoji(700041815327506532)
        cross = self.bot.get_emoji(700041862206980146)
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=200, check=reactionCheck)
        except:
            embed=discord.Embed(title="PROMPT TIMED OUT", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `demote` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        else:
            if reaction.emoji == tick:
                pass
            elif reaction.emoji == cross:
                embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `demote` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoSystems")
                await ctx.send(embed=embed)
                return


            group = await client.get_group(id)
            try:
                await group.demote(user_Id)
            except robloxapi.utils.errors.BadStatus:
                embed=discord.Embed(title="YOU CANNOT CHANGE THIS ACCOUNTS RANK, PROMPT CANCELLED", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `demote` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoSystems")
                await ctx.send(embed=embed)
                return

            embed=discord.Embed(title="USER WAS SUCCESSFULLY DEMOTED", color=0x1de97b)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)


    @commands.check(configured)
    @commands.command()
    async def showrank(self, ctx, user):
        """
        Displays the users rank in the set group.
        """


        with open('data/groupdata.json') as f:
            data = json.load(f)
        cookie = data[f"{ctx.guild.id}"]["Cookie"]
        id = data[f"{ctx.guild.id}"]["ID"]

        client = robloxapi.Client(cookie)
        RobloxUser_object = await client.get_user(name=f"{user}")
        try:
            x = await RobloxUser_object.get_role_in_group(id)
        except robloxapi.utils.errors.NotFound:
            embed=discord.Embed(title="THIS USER IS NOT IN THE GROUP, PROMPT CANCELLED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `demote` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        else:
            embed=discord.Embed(title="USER DATA", color=0x36393e)
            embed.add_field(name="<:logo:700042045447864520>", value=f"User-rank: `{x.name}`\nUser-rankID: `{x.id}`", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            msg = await ctx.send(embed=embed)

    @commands.has_permissions(manage_guild=True)
    @commands.check(configured)
    @commands.command()
    async def fire(self, ctx, user):
        """
        Demotes a user to the lowest rank.
        """
        def reactionCheck(reaction, user):
            if user == ctx.author and reaction.emoji == tick:
                return True
            if user == ctx.author and reaction.emoji == cross:
                return True
        with open('data/groupdata.json') as f:
            data = json.load(f)

        cookie = data[f"{ctx.guild.id}"]["Cookie"]
        id = data[f"{ctx.guild.id}"]["ID"]

        user_request = requests.get(url=f'https://api.roblox.com/users/get-by-username?username={user}')
        user_json = user_request.json()
        try:
            user_name = user_json["Username"]
            user_Id = user_json["Id"]
        except KeyError:
            embed=discord.Embed(title="THIS USER DOES NOT EXIST", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `fire` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return

        roles_request = requests.get(url=f'https://groups.roblox.com/v1/groups/{id}/roles')
        roles_json = roles_request.json()
        lst = []
        for role in roles_json.get('roles'):
            lst.append(str(role["rank"]))
        lst.sort()

        for role in roles_json.get('roles'):
            if int(role["rank"]) == int(lst[1]):
                rankingRole = role["name"]
                rankingRoleID = role["id"]

        client = robloxapi.Client(cookie)
        RobloxUser_object = await client.get_user(name=f"{user_name}")
        try:
            x = await RobloxUser_object.get_role_in_group(id)
        except robloxapi.utils.errors.NotFound:
            embed=discord.Embed(title="THIS USER IS NOT IN THE GROUP, PROMPT CANCELLED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `fire` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return

        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value=f"Please confirm that this is the correct data.\n`Account-name`: {user_name}\n`Account-ID`: {user_Id}\n`Currant-rank`: {x.name}\n`New-rank`: {rankingRole}\n\nsay **cancel** to cancel.", inline=False)
        embed.set_footer(text="This prompt will automatically cancel in 200 seconds.")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('<:tick:700041815327506532>')
        await msg.add_reaction('<:rcross:700041862206980146>')
        tick = self.bot.get_emoji(700041815327506532)
        cross = self.bot.get_emoji(700041862206980146)
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=200, check=reactionCheck)
        except:
            embed=discord.Embed(title="PROMPT TIMED OUT", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `fire` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        else:
            if reaction.emoji == tick:
                pass
            elif reaction.emoji == cross:
                embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `fire` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoSystems")
                await ctx.send(embed=embed)
                return


            group = await client.get_group(id)
            try:
                await group.set_rank(user_Id, rankingRoleID)
            except robloxapi.utils.errors.BadStatus:
                embed=discord.Embed(title="YOU CANNOT CHANGE THIS ACCOUNTS RANK, PROMPT CANCELLED", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `fire` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoSystems")
                await ctx.send(embed=embed)
                return

            embed=discord.Embed(title="USER WAS SUCCESSFULLY FIRED", color=0x1de97b)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)

    @commands.has_permissions(manage_guild=True)
    @commands.check(configured)
    @commands.command()
    async def shout(self, ctx, *, message):

        def reactionCheck(reaction, user):
            if user == ctx.author and reaction.emoji == tick:
                return True
            if user == ctx.author and reaction.emoji == cross:
                return True

        with open('data/groupdata.json') as f:
            data = json.load(f)

        cookie = data[f"{ctx.guild.id}"]["Cookie"]
        id = data[f"{ctx.guild.id}"]["ID"]
        client = robloxapi.Client(cookie)
        group = await client.get_group(id)
        try:
            embed=discord.Embed(title="PROMPT", color=0x36393e)
            embed.add_field(name="<:logo:700042045447864520>", value=f"Please confirm that this is the correct data.\n`Message`: {message}", inline=False)
            embed.set_footer(text="This prompt will automatically cancel in 200 seconds.")
            msg = await ctx.send(embed=embed)
        except:
            embed=discord.Embed(title="I DON'T HAVE PERMISSIONS TO DO THIS/MESSAGE TO LONG, PROMPT CANCELLED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `shout` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        await msg.add_reaction('<:tick:700041815327506532>')
        await msg.add_reaction('<:rcross:700041862206980146>')
        tick = self.bot.get_emoji(700041815327506532)
        cross = self.bot.get_emoji(700041862206980146)

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=200, check=reactionCheck)
        except:
            embed=discord.Embed(title="PROMPT TIMED OUT", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `shout` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        else:
            if reaction.emoji == tick:
                pass
            elif reaction.emoji == cross:
                embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `shout` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoSystems")
                await ctx.send(embed=embed)
                return

        try:
            members = await group.post_shout(message)
        except:
            embed=discord.Embed(title="I DON'T HAVE PERMISSIONS TO DO THIS/MESSAGE TO LONG, PROMPT CANCELLED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `shout` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return

        embed=discord.Embed(title="SHOUT WAS POSTED SUCCESFULLY", color=0x1de97b)
        embed.set_footer(text="All assets owned by RoSystems")
        await ctx.send(embed=embed)





def setup(bot):
    bot.add_cog(Roblox(bot))
