import discord
from discord.ext import commands
import time
import sys
import os
import asyncio
import random
from discord.utils import get
class utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(kick_members=True)
    @commands.command(description="Kicks a user from the discord server.")
    async def kick(self, ctx, member:discord.Member=None, *, reason=None):
        """
        Kicks a user from the discord server.
        """
        def reactionCheck(reaction, user):
            if user == ctx.author and reaction.emoji == tick:
                return True
            if user == ctx.author and reaction.emoji == cross:
                return True
        if not reason:
            reason = f'No reason was given'

        if not member:
            embed=discord.Embed(title="PLEASE PROVIDE ALL COMMAND AURGUMENTS", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `help utility` for more information.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return


        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value=f"Please confirm that this is the correct data.\n`User-name`: {member}\n`User-ID`: {member.id}\n`Reason`: {reason}\n`Action`: Kick", inline=False)
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
            embed.add_field(name="<:logo:700042045447864520>", value="Type `kick` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        else:
            if reaction.emoji == tick:
                pass
            elif reaction.emoji == cross:
                embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `kick` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoSystems")
                await ctx.send(embed=embed)
                return
        try:
            embed=discord.Embed(title=f"KICKED FROM {ctx.guild.name}", color=0x45f182)
            embed.add_field(name="<:logo:700042045447864520>", value=f"Action Data:\n`Kicked-by`: {ctx.author}\n`Kicked-for`: {reason}")
            await member.send(embed=embed)
        except:
            pass
        try:
            await ctx.guild.kick(member, reason=reason)
        except commands.MissingPermissions:
            await ctx.send("<:rcross:700041862206980146> You/I don't have permissions to run this command!.")

        embed=discord.Embed(title=f"ACTION COMPLETED", color=0x1de97b)
        await ctx.send(embed=embed)

    @commands.has_permissions(ban_members=True)
    @commands.command(description="Bans a user from the discord server.")
    async def ban(self, ctx, member:discord.Member=None, *, reason=None):
        """
        Bans a user from the discord server.
        """
        def reactionCheck(reaction, user):
            if user == ctx.author and reaction.emoji == tick:
                return True
            if user == ctx.author and reaction.emoji == cross:
                return True
        if not reason:
            reason = f'No reason was given'

        if not member:
            embed=discord.Embed(title="PLEASE PROVIDE ALL COMMAND AURGUMENTS", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `help utility` for more information.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return


        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value=f"Please confirm that this is the correct data.\n`User-name`: {member}\n`User-ID`: {member.id}\n`Reason`: {reason}\n`Action`: Ban", inline=False)
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
            embed.add_field(name="<:logo:700042045447864520>", value="Type `ban` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        else:
            if reaction.emoji == tick:
                pass
            elif reaction.emoji == cross:
                embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `ban` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoSystems")
                await ctx.send(embed=embed)
                return
        try:
            embed=discord.Embed(title=f"BANNED FROM {ctx.guild.name}", color=0x45f182)
            embed.add_field(name="<:logo:700042045447864520>", value=f"Action Data:\n`Banned-by`: {ctx.author}\n`Banned-for`: {reason}")
            await member.send(embed=embed)
        except:
            pass
        try:
            await ctx.guild.ban(member, reason=reason)
        except commands.MissingPermissions:
            await ctx.send("<:rcross:700041862206980146> You/I don't have permissions to run this command!.")
        embed=discord.Embed(title=f"ACTION COMPLETED", color=0x1de97b)
        await ctx.send(embed=embed)
    @comands.max_concurrency(number, per=<BucketType.default: 0>, *, wait=False)
    @commands.has_permissions(ban_members=True)
    @commands.command(description="Unbans a user from the discord server.")
    async def unban(self, ctx, id=None):
        """
        Unbans a user from the discord server.
        """
        def reactionCheck(reaction, user):
            if user == ctx.author and reaction.emoji == tick:
                return True
            if user == ctx.author and reaction.emoji == cross:
                return True
        try:
            id = int(id)
        except:
            embed=discord.Embed(title="PLEASE PROVIDE A VALID ID", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `help utility` for more information.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        if not id:
            embed=discord.Embed(title="PLEASE PROVIDE ALL COMMAND AURGUMENTS", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `help utility` for more information.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return

        try:
            member = await self.bot.fetch_user(id)
        except:
            embed=discord.Embed(title="USER NOT FOUND, PROMPT TERMINATED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `unban` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value=f"Please confirm that this is the correct data.\n`User-name`: {member}\n`User-ID`: {member.id}\n`Action`: UnBan", inline=False)
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
            embed.add_field(name="<:logo:700042045447864520>", value="Type `unban` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        else:
            if reaction.emoji == tick:
                pass
            elif reaction.emoji == cross:
                embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `unban` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoSystems")
                await ctx.send(embed=embed)
                return
        try:
            await ctx.guild.unban(member)
        except commands.MissingPermissions:
            await ctx.send("<:rcross:700041862206980146> You/I don't have permissions to run this command!.")
        embed=discord.Embed(title=f"ACTION COMPLETED", color=0x1de97b)
        await ctx.send(embed=embed)

    @commands.has_permissions(manage_messages=True)
    @commands.command(description="Purges the specified ammount of messages.")
    async def purge(self, ctx, num: int, target: discord.Member=None):
        """
        Purges the specified ammount of messages.
        """
        if num > 500 or num < 0:
            return await ctx.send("<:rcross:700041862206980146> **Invalid amount. Maximum is 500.**")
        def msgcheck(amsg):
            if target:
               return amsg.author.id == target.id
            return True
        num = num + 1
        deleted = await ctx.channel.purge(limit=num, check=msgcheck)
        num = num - 1
        await ctx.send(f'`Deleted {num} messages for you.`', delete_after=10)

    @commands.has_permissions(manage_messages=True)
    @commands.command(description="Mutes a user for a specified ammount of time.")
    async def mute(self, ctx, member: discord.Member, time: int=None):
        """
        Mutes a user for a specified ammount of time.
        """
        def reactionCheck(reaction, user):
            if user == ctx.author and reaction.emoji == tick:
                return True
            if user == ctx.author and reaction.emoji == cross:
                return True
        if not time or not member:
            embed=discord.Embed(title="PLEASE PROVIDE ALL COMMAND AURGUMENTS", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `help utility` for more information.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return

        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value=f"Please confirm that this is the correct data.\n`User-name`: {member}\n`User-ID`: {member.id}\n`Time`: {time} seconds\n`Action`: Mute", inline=False)
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
            embed.add_field(name="<:logo:700042045447864520>", value="Type `mute` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        else:
            if reaction.emoji == tick:
                pass
            elif reaction.emoji == cross:
                embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `mute` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoSystems")
                await ctx.send(embed=embed)
                return

        perms = discord.Permissions(send_messages=False, read_messages=True)
        valid_roles = ['Muted', 'MUTED', 'muted']
        x = None
        for i in ctx.guild.roles:
            # await ctx.send(type(i))
            if i.name in valid_roles:
                x = i
        if not x:
            await ctx.guild.create_role(name='Muted', permissions=perms)
        else:
            Muted = discord.utils.get(member.guild.roles, name=f'{x}')

        embed=discord.Embed(title=f"ACTION COMPLETED", description='User will be automatically unmuted after designated time.', color=0x1de97b)
        await ctx.send(embed=embed)

        await member.add_roles(Muted)
        await asyncio.sleep(time)
        await member.remove_roles(Muted)

    @commands.has_permissions(manage_messages=True)
    @commands.command(description="Unmutes a user.")
    async def unmute(self, ctx, member: discord.Member=None):
        """
        Unmutes a user.
        """
        if not member:
            pass
        def reactionCheck(reaction, user):
            if user == ctx.author and reaction.emoji == tick:
                return True
            if user == ctx.author and reaction.emoji == cross:
                return True

        embed=discord.Embed(title="PROMPT", color=0x36393e)
        embed.add_field(name="<:logo:700042045447864520>", value=f"Please confirm that this is the correct data.\n`User-name`: {member}\n`User-ID`: {member.id}\n`Action`: UnMute", inline=False)
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
            embed.add_field(name="<:logo:700042045447864520>", value="Type `unmute` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        else:
            if reaction.emoji == tick:
                pass
            elif reaction.emoji == cross:
                embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
                embed.add_field(name="<:logo:700042045447864520>", value="Type `unmute` to restart prompt.", inline=False)
                embed.set_footer(text="All assets owned by RoSystems")
                await ctx.send(embed=embed)
                return

        perms = discord.Permissions(send_messages=False, read_messages=True)
        valid_roles = ['Muted', 'MUTED', 'muted']
        x = None
        for i in member.roles:
            # await ctx.send(type(i))
            if i.name in valid_roles:
                x = i
        if not x:
            embed=discord.Embed(title="THIS USER IS NOT MUTED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `unmute` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return
        else:
            Muted = discord.utils.get(member.guild.roles, name=f'{x}')

        await member.remove_roles(Muted)


        embed=discord.Embed(title=f"ACTION COMPLETED", color=0x1de97b)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(utility(bot))
