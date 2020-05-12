import discord
from discord.ext import commands
import time
import sys
import os


class Errors(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("<:rcross:700041862206980146> You don't have permissions to run this command!.")
            return
        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("<:rcross:700041862206980146> You did not give all peramiters for that command!.")
            return
        if isinstance(error, commands.BadArgument):
            await ctx.send("<:rcross:700041862206980146> You did not give valid peramiters for that command!.")
            return
        if isinstance(error, commands.NotOwner):
            await ctx.send("<:rcross:700041862206980146> You must own this bot to use that command!.")
            return
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("<:rcross:700041862206980146> Please provide all aurguments!.")
            return
        if isinstance(error, commands.MaxConcurrencyReached):
            await ctx.send("<:rcross:700041862206980146> Please wait for the previous command to finish before executing it again!.")
            return

        else:
            Guild = self.bot.get_guild(699991602126389248)
            channel = Guild.get_channel(706942712242372679)
            embed=discord.Embed(title="AN ERROR OCCURED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Oh no! It seems you have discovered an error, don't worry, it has been reported to our development team.", inline=False)
            embed.set_footer(text="All assets owned by RoServices")
            await ctx.send(embed=embed)

            embed=discord.Embed(title="NEW ERROR", color=0xee6551)
            embed.add_field(name="Guild-ID:", value=f"`{ctx.guild.id}`", inline=False)
            embed.add_field(name="Command:", value=f"`{ctx.message.content}`", inline=False)
            embed.add_field(name="Error:", value=f"`{error}`", inline=False)
            embed.set_footer(text="All assets owned by RoServices")
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Errors(bot))
