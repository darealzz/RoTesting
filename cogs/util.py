import discord
from discord.ext import commands
import time
import sys
import os
import asyncio
import random
from discord.utils import get
class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def reportbug(ctx):
    def reactionCheck(reaction, user):
        if user == ctx.author and reaction.emoji == tick:
            return True
        if user == ctx.author and reaction.emoji == cross:
            return True
    def check(m):
        return m.author == ctx.author
    embed=discord.Embed(title="**PROMPT**", description=f"", color=0x36393e)
    embed.set_author(name=f"{ctx.message.author}", icon_url=f'{ctx.author.avatar_url_as(format="png")}')
    embed.add_field(name="<:logo:700042045447864520>", value=f"Please describe your issue with as many details as possible, please also include 'how to replicate this.' If you have any pictures please use a LINK.", inline=False)
    await ctx.send(embed=embed)
    bug = await self.bot.wait_for('message', timeout=200, check=check)
    guild = ctx.guild
    id = guild.id
    embed=discord.Embed(title="BUG REPORT", color=0x36393e)
    embed.set_author(name=f"{ctx.message.author}", icon_url=f'{ctx.author.avatar_url_as(format="png")}')
    embed.add_field(name="Guild:", value=f"{guild}", inline=True)
    embed.add_field(name="Guild-id:", value=f"{id}", inline=False)
    embed.add_field(name="Reporter-tag:", value=f"{ctx.author.mention}", inline=True)
    embed.add_field(name="Reporter:", value=f"{ctx.author}", inline=True)
    embed.add_field(name="Reporter-id:", value=f"{ctx.author.id}", inline=True)
    embed.add_field(name="Bug:", value=f"{bug.content}", inline=False)
    embed.set_footer(text="All assets owned by RoSystems")
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
        embed.set_footer(text="All assets owned by RoServices")
        await ctx.send(embed=embed)
        return
    if bug.content.upper() == 'CANCEL':
        embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
        embed.add_field(name="<:logo:700042045447864520>", value="Type `reportbug` to restart prompt.", inline=False)
        embed.set_footer(text="All assets owned by RoServices")
        await ctx.send(embed=embed)
        return
    else:
        if reaction.emoji == tick:
            embed = discord.Embed(title=f"**BUG REPORTED**", color=0x33b404)
            embed.add_field(name="<:logo:700042045447864520>", value=f"The bug has been reported to the developers.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)

            guild = ctx.guild
            id = guild.id
            guild1 = self.bot.get_guild(699991602126389248)
            channel = guild1.get_channel(702884858770489344)
            embed=discord.Embed(title="BUG REPORTED", color=0x36393e)
            embed.set_author(name=f"{ctx.message.author}", icon_url=f'{ctx.author.avatar_url_as(format="png")}')
            embed.add_field(name="Guild:", value=f"{guild}", inline=True)
            embed.add_field(name="Guild-id:", value=f"{id}", inline=False)
            embed.add_field(name="Reporter-tag:", value=f"{ctx.author.mention}", inline=True)
            embed.add_field(name="Reporter:", value=f"{ctx.author}", inline=True)
            embed.add_field(name="Reporter-id:", value=f"{ctx.author.id}", inline=True)
            embed.add_field(name="Bug:", value=f"{bug.content}", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await channel.send(embed=embed)
            pass
        elif reaction.emoji == cross:
            embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `reportbug` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoServices")
            await ctx.send(embed=embed)
            return

@commands.command()
async def invite(ctx):
    await ctx.author.send('<:logo:700042045447864520>Hey there!\n\n<:logo:700042045447864520>Need support? Check out our support server: https://discord.gg/7pusanw\n\n<:logo:700042045447864520>Want the bot for yourself? Click the link and invite it to your server today! https://discordapp.com/oauth2/authorize?bot_id=700020186371326054&scope=bot&permissions=8\n\n<:logo:700042045447864520>Our team hopes you enjoy our bot, we have put alot of effort into this.')
    await ctx.send(f'{ctx.author.mention}, Check your DMs!')


# Mute command
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def Mute(ctx, member : discord.Member):
    role = discord.utils.get(member.guild.roles, name='Muted')
    try:
        embed = discord.Embed(title="You have been muted!", description=" ", color=0xD30000)
        embed.add_field(name="Muted-by:", value=f"{ctx.author}", inline=False)
        embed.set_footer(text="All assets owned by RoSystems")
        await member.send(embed=embed)
    except discord.Forbidden:
            pass
    await member.add_roles(role)
    embed = discord.Embed(title="User `@"f'{member}'"` Muted!", description=" ", color=0x5ED500)
    embed.set_author(name=f"{ctx.message.author}", icon_url=f'{ctx.author.avatar_url_as(format="png")}')
    embed.add_field(name="Muted-by:", value=f"{ctx.author}", inline=False)
    embed.set_footer(text="All assets owned by RoSystems")
    await ctx.send(embed=embed)

    logs = self.bot.get_channel(701944694174908497)
    embed=discord.Embed(title="USER MUTED", color=0x00E5E5)
    embed.set_author(name=f"{ctx.message.author}", icon_url=f'{ctx.author.avatar_url_as(format="png")}')
    embed.add_field(name="Muted:", value=f"{member}", inline=False)
    embed.add_field(name="Muted-by:", value=f"{ctx.author}", inline=False)
    embed.set_footer(text="All assets owned by RoSystems")
    await logs.send(embed=embed)
#############################################################


# Unmute command
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def Unmute(ctx, member : discord.Member):
    role = discord.utils.get(member.guild.roles, name='Muted')
    await member.remove_roles(role)
    embed = discord.Embed(title="User `@"f'{member}'"` Unmuted!", description=" ", color=0x5ED500)
    embed.set_author(name=f"{ctx.message.author}", icon_url=f'{ctx.author.avatar_url_as(format="png")}')
    embed.set_footer(text="All assets owned by RoSystems")
    await ctx.send(embed=embed)
#############################################################

# Ban Command
@commands.command()
@commands.has_permissions(ban_members=True)
async def Ban(ctx, member : discord.Member, *,reason=None):
    embed = discord.Embed(title=f"Are you sure you want to Ban `{member}` ?", description=f" ", color=0x00E5E5)
    embed.set_footer(text="All assets owned by RoSystems")

    sure = await ctx.send(embed=embed)
    await sure.add_reaction('\U00002705')
    await sure.add_reaction('\U0000274c')
    def check(reaction, user):
            if user == ctx.message.author and str(reaction.emoji) == '\U00002705':
                return True
            if user == ctx.message.author and str(reaction.emoji) == '\U0000274c':
                return True
    reaction, user = await self.bot.wait_for('reaction_add', check=check)
    if str(reaction.emoji) == '\U00002705':
        try:
            embed = discord.Embed(title='You have been Banned!', color=0xD30000)
            embed.add_field(name=f'Reason:', value=f'{reason}', inline=True)
            embed.add_field(name="Banned-by:", value=f"{ctx.author}", inline=True)
            embed.set_footer(text="All assets owned by RoSystems")
            await member.send(embed=embed)
        except discord.Forbidden:
            pass
        await member.ban(reason=reason)
        embed = discord.Embed(title='User Banned!', color=0x5ED500)
        embed.set_author(name=f"{ctx.message.author}", icon_url=f'{ctx.author.avatar_url_as(format="png")}')
        embed.add_field(name=f'**User: **', value=f'{member}', inline=True)
        embed.add_field(name=f'**Reason: **', value=f'{reason}', inline=True)
        embed.set_footer(text="All assets owned by RoSystems")
        await ctx.send(embed=embed)

        logs = self.bot.get_channel(701944694174908497)
        embed=discord.Embed(title="USER BANNED", color=0x00E5E5)
        embed.set_author(name=f"{ctx.message.author}", icon_url=f'{ctx.author.avatar_url_as(format="png")}')
        embed.add_field(name="Banned:", value=f"{member}", inline=False)
        embed.add_field(name="Reason:", value=f"{reason}", inline=False)
        embed.add_field(name="Banned-by:", value=f"{ctx.author}", inline=False)
        embed.set_footer(text="All assets owned by RoSystems")
        await logs.send(embed=embed)
    if str(reaction.emoji) == '\U0000274c':
        embed = discord.Embed(title=f"Command cancelled!", description=f"", color=0xD30000)
        embed.set_footer(text="All assets owned by RoSystems")
        await ctx.send(embed=embed)
#############################################################

# Unban command
@commands.command()
@commands.has_permissions(ban_members=True)
async def Unban(ctx, *, member):
    bans = await ctx.guild.bans()
    member_name, member_hash = member.split('#')

    for ban_entry in bans:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_hash):
            await ctx.guild.unban(user)
            embed = discord.Embed(title='User Unbanned!', color=0x5ED500)
            embed.add_field(name="Unbanned:", value=f"{user.name}#{user.discriminator}", inline=True)
            embed.add_field(name="Unbanned-by:", value=f"{ctx.author}", inline=True)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)

            logs = self.bot.get_channel(701944694174908497)
            embed=discord.Embed(title="USER UNBANNED", color=0x00E5E5)
            embed.set_author(name=f"{ctx.message.author}", icon_url=f'{ctx.author.avatar_url_as(format="png")}')
            embed.add_field(name="Unbanned:", value=f"{user.name}#{user.discriminator}", inline=False)
            embed.add_field(name="Unbanned-by:", value=f"{ctx.author}", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await logs.send(embed=embed)
#############################################################

# Kick command
@commands.command()
@commands.has_permissions(kick_members=True)
async def Kick(ctx, member : discord.Member, *,reason=None):
    embed = discord.Embed(title=f"Are you sure you want to Kick `{member}` ?", description=f" ", color=0x00E5E5)
    embed.set_footer(text="All assets owned by RoSystems")

    sure = await ctx.send(embed=embed)
    await sure.add_reaction('\U00002705')
    await sure.add_reaction('\U0000274c')
    def check(reaction, user):
            if user == ctx.message.author and str(reaction.emoji) == '\U00002705':
                return True
            if user == ctx.message.author and str(reaction.emoji) == '\U0000274c':
                return True
    reaction, user = await self.bot.wait_for('reaction_add', check=check)
    if str(reaction.emoji) == '\U00002705':
        try:
            embed = discord.Embed(title='You have been Kicked!', color=0xD30000)
            embed.add_field(name=f'Reason:', value=f'{reason}', inline=True)
            embed.add_field(name="Kicked-by:", value=f"{ctx.author}", inline=True)
            embed.set_footer(text="All assets owned by RoSystems")
            await member.send(embed=embed)
        except discord.Forbidden:
            pass
        await member.kick(reason=reason)
        embed = discord.Embed(title='User Kicked!', color=0x5ED500)
        embed.set_author(name=f"{ctx.message.author}", icon_url=f'{ctx.author.avatar_url_as(format="png")}')
        embed.add_field(name=f'**User: **', value=f'{member}', inline=True)
        embed.add_field(name=f'**Reason: **', value=f'{reason}', inline=True)
        embed.set_footer(text="All assets owned by RoSystems")
        await ctx.send(embed=embed)

        logs = self.bot.get_channel(701944694174908497)
        embed=discord.Embed(title="USER KICKED", color=0x00E5E5)
        embed.set_author(name=f"{ctx.message.author}", icon_url=f'{ctx.author.avatar_url_as(format="png")}')
        embed.add_field(name="Kicked:", value=f"{member}", inline=False)
        embed.add_field(name="Reason:", value=f"{reason}", inline=False)
        embed.add_field(name="Kicked-by:", value=f"{ctx.author}", inline=False)
        embed.set_footer(text="All assets owned by RoSystems")
        await logs.send(embed=embed)
    if str(reaction.emoji) == '\U0000274c':
        embed = discord.Embed(title=f"Command cancelled!", description=f"", color=0xD30000)
        embed.set_footer(text="All assets owned by RoSystems")
        await ctx.send(embed=embed)
#############################################################

# Clear command
@commands.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, num: int, target: discord.Member=None):
    if num > 500 or num < 0:
        return await ctx.send("`Invalid amount. Maximum is 500.`")
    def msgcheck(amsg):
        if target:
           return amsg.author.id == target.id
        return True
    num = num + 1
    deleted = await ctx.channel.purge(limit=num, check=msgcheck)
    num = num - 1
    await ctx.send(f'`Deleted {num} messages for you.`', delete_after=10)
#############################################################

# Nuke command
@commands.command()
@commands.is_owner()
async def nuke(ctx):
    await ctx.channel.purge(limit=99999999999999)
    await ctx.send('https://media.giphy.com/media/oe33xf3B50fsc/giphy.gif')
    await ctx.send(':bomb: Channel nuked :bomb:')
#############################################################

def setup(bot):
    bot.add_cog(Utility(bot))
