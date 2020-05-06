import asyncio
import discord
from discord.ext import tasks, commands
import json
import os
import random
import jishaku
import psycopg2

bot = commands.Bot(command_prefix='$', case_insensitive=True)
#bot.remove_command("help")
bot.load_extension('jishaku')
bot.remove_command("help")
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")

# con = psycopg2.connect(
#             host = "sikli",
#             database = "RoSystems",
#             user = "postgres",
#             password = "postgres")
#
# cur = con.cursor()


@bot.event
async def on_ready():
    print("ready")
    change_status.start()

@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.users)} Users"))


@bot.event
async def on_guild_join(guild):
    channel = bot.get_channel(700309585264640000)
    if not guild.icon:
        embed=discord.Embed(title="NEW GUILD JOIN", color=0x2fdbff)
        #embed.set_thumbnail(url=f"{guild.icon}")
        embed.add_field(name="Guild Name:", value=f"{guild.name}", inline=False)
        embed.add_field(name="Guild ID:", value=f"{guild.id}", inline=False)
        embed.add_field(name="Guild Owner:", value=f"{guild.owner}", inline=False)
        embed.add_field(name="Guild OwnerID:", value=f"{guild.owner_id}", inline=False)
        embed.set_footer(text="Assets owned by RoSystems.")
        await channel.send(embed=embed)
    else:
        embed=discord.Embed(title="NEW GUILD JOIN", color=0x2fdbff)
        embed.set_thumbnail(url=f"{guild.icon_url}")
        embed.add_field(name="Guild Name:", value=f"{guild.name}", inline=False)
        embed.add_field(name="Guild ID:", value=f"{guild.id}", inline=False)
        embed.add_field(name="Guild Owner:", value=f"{guild.owner}", inline=False)
        embed.add_field(name="Guild OwnerID:", value=f"{guild.owner_id}", inline=False)
        embed.set_footer(text="Assets owned by RoSystems.")
        await channel.send(embed=embed)
        #for element in guild.channels:
            #print(element)
        NeWkchannel = await guild.create_text_channel('roservices')


        await NeWkchannel.send('<:logo:700042045447864520> Thank you for using RoServices!\n\n:exclamation: To see a full list of commands, use `$help`\n:gear: To setup your server with RoServices type `$setup`\n:question: If your require assistance, join our support server! https://discord.gg/DmU9gEv')



@bot.event
async def on_command_error(ctx, error):
    Guild = bot.get_guild(699991602126389248)
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


@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    try:
        bot.load_extension(f"cogs.{extension}")
    except commands.errors.ExtensionAlreadyLoaded:
        await ctx.send(f"<:rcross:700041862206980146> | **Cog already loaded: `{extension}`**")
    else:
        await ctx.send(f"<:tick:700041815327506532> | **Loaded Cog: `{extension}`**")

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    try:
        bot.unload_extension(f"cogs.{filename[:-3]}")
    except commands.errors.ExtensionNotLoaded:
        await ctx.send(f"<:rcross:700041862206980146> | **Cog not loaded: `{extension}`**")
    else:
        bot.load_extension(f"cogs.{filename[:-3]}")
        await ctx.send(f"<:tick:700041815327506532> | **Realoded Cog: `{extension}`**")

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    try:
        bot.unload_extension(f"cogs.{extension}")
    except commands.errors.ExtensionNotLoaded:
        await ctx.send(f"<:rcross:700041862206980146> | **Cog not loaded: `{extension}`**")
    else:
        await ctx.send(f"<:tick:700041815327506532> | **Unloaded Cog: `{extension}`**")

@bot.command()
@commands.is_owner()
async def r(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                bot.unload_extension(f"cogs.{filename[:-3]}")
            except commands.errors.ExtensionNotLoaded:
                await ctx.send(f"<:rcross:700041862206980146> | **Cog not loaded: `{filename[:-3]}`**")
            else:
                bot.load_extension(f"cogs.{filename[:-3]}")
                await ctx.send(f"<:tick:700041815327506532> | **Realoded Cog: `{filename[:-3]}`**")
    #await ctx.send(f"<:tick:700041815327506532> | `Reloaded the cogs`")

@bot.command()
@commands.is_owner()
async def cogs(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await ctx.send(f"`{filename[:-3]}`")

# con.close()
bot.run('NzAwMDIwMTg2MzcxMzI2MDU0.XqBLWg.KdyEFkVqeeLpC4VMLrWBLlbN7Lg')
