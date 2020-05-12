import asyncio
import discord
from discord.ext import tasks, commands
import json
import os
import random
import jishaku
import discord


def get_prefix(bot, message):
    with open('notusing/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True)

bot.remove_command("help")


@bot.event
async def on_guild_join(guild):
    with open("notusing/prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = "$"
    with open("notusing/prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open("notusing/prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))
    with open("notusing/prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@bot.command()
@commands.has_permissions(manage_guild=True)
async def setprefix(ctx, prefix):

    def reactionCheck(reaction, user):
        if user == ctx.author and reaction.emoji == tick:
            return True
        if user == ctx.author and reaction.emoji == cross:
            return True

    with open("notusing/prefixes.json", "r") as f:
        prefixes = json.load(f)
    old = prefixes[str(ctx.guild.id)]
    prefixes[str(ctx.guild.id)] = prefix

    embed=discord.Embed(title="PROMPT", color=0x36393e)
    embed.add_field(name="<:logo:700042045447864520>", value=f'Please confirm that this is the correct data.\n`Old-Prefix`: {old}\n`New-Prefix`: {prefix}', inline=False)
    embed.set_footer(text="This prompt will automatically cancel in 200 seconds.")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('<:tick:700041815327506532>')
    await msg.add_reaction('<:rcross:700041862206980146>')
    tick = bot.get_emoji(700041815327506532)
    cross = bot.get_emoji(700041862206980146)
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=200, check=reactionCheck)
    except:
        embed=discord.Embed(title="PROMPT TIMED OUT", color=0xee6551)
        embed.add_field(name="<:logo:700042045447864520>", value="Type `setprefix` to restart prompt.", inline=False)
        embed.set_footer(text="All assets owned by RoSystems")
        await ctx.send(embed=embed)
        return
    else:
        if reaction.emoji == tick:
            pass
        elif reaction.emoji == cross:
            embed=discord.Embed(title="PROMPT CANCELLED", color=0xee6551)
            embed.add_field(name="<:logo:700042045447864520>", value="Type `setprefix` to restart prompt.", inline=False)
            embed.set_footer(text="All assets owned by RoSystems")
            await ctx.send(embed=embed)
            return

    with open("notusing/prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

    embed=discord.Embed(title="ACTION COMPLETED SUCCESFULLY", color=0x1de97b)
    embed.set_footer(text="All assets owned by RoSystems")
    await ctx.send(embed=embed)
    return


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
    change_statuss.start()
    change_statusss.start()

@tasks.loop(seconds=20)
async def change_status():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.users)} Users"))
@tasks.loop(seconds=40)
async def change_statuss():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} Servers"))
@tasks.loop(seconds=60)
async def change_statusss():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"$help | $setup | $invite"))

@bot.event
async def on_guild_join(guild):
    NeWkchannel = await guild.create_text_channel('roservices')

    asd = await NeWkchannel.create_invite(max_age=0, max_user=0, reason='RoServices staff usage.')
    channel = bot.get_channel(700309585264640000)
    if not guild.icon:
        embed=discord.Embed(title="NEW GUILD JOIN", color=0x2fdbff)
        #embed.set_thumbnail(url=f"{guild.icon}")
        embed.add_field(name="Guild Name:", value=f"{guild.name}", inline=False)
        embed.add_field(name="Guild ID:", value=f"{guild.id}", inline=False)
        embed.add_field(name="Guild Owner:", value=f"{guild.owner}", inline=False)
        embed.add_field(name="Guild OwnerID:", value=f"{guild.owner_id}", inline=False)
        embed.add_field(name="Guild Invite:", value=f'https://discord.gg/{asd.code}', inline=False)
        embed.set_footer(text="Assets owned by RoSystems.")
        await channel.send(embed=embed)
    else:
        embed=discord.Embed(title="NEW GUILD JOIN", color=0x2fdbff)
        embed.set_thumbnail(url=f"{guild.icon_url}")
        embed.add_field(name="Guild Name:", value=f"{guild.name}", inline=False)
        embed.add_field(name="Guild ID:", value=f"{guild.id}", inline=False)
        embed.add_field(name="Guild Owner:", value=f"{guild.owner}", inline=False)
        embed.add_field(name="Guild OwnerID:", value=f"{guild.owner_id}", inline=False)
        embed.add_field(name="Guild Invite:", value=f'https://discord.gg/{asd.code}', inline=False)
        embed.set_footer(text="Assets owned by RoSystems.")
        await channel.send(embed=embed)
        #for element in guild.channels:
            #print(element)
    await NeWkchannel.send('<:logo:700042045447864520> Thank you for using RoServices!\n\n:exclamation: To see a full list of commands, use `$help`\n:gear: To setup your server with RoServices type `$setup`\n:question: If your require assistance, join our support server! https://discord.gg/DmU9gEv')




@bot.command(description="Owner only.")
@commands.is_owner()
async def load(ctx, extension):
    """
    Loads cogs.
    """
    try:
        bot.load_extension(f"cogs.{extension}")
    except commands.errors.ExtensionAlreadyLoaded:
        await ctx.send(f"<:rcross:700041862206980146> | **Cog already loaded: `{extension}`**")
    else:
        await ctx.send(f"<:tick:700041815327506532> | **Loaded Cog: `{extension}`**")

@bot.command(description="Owner only.")
@commands.is_owner()
async def reload(ctx, extension):
    """
    Reloads specific cog.
    """
    try:
        bot.unload_extension(f"cogs.{filename[:-3]}")
    except commands.errors.ExtensionNotLoaded:
        await ctx.send(f"<:rcross:700041862206980146> | **Cog not loaded: `{extension}`**")
    else:
        bot.load_extension(f"cogs.{filename[:-3]}")
        await ctx.send(f"<:tick:700041815327506532> | **Realoded Cog: `{extension}`**")

@bot.command(description="Owner only.")
@commands.is_owner()
async def unload(ctx, extension):
    """
    Unloads specific cog.
    """
    try:
        bot.unload_extension(f"cogs.{extension}")
    except commands.errors.ExtensionNotLoaded:
        await ctx.send(f"<:rcross:700041862206980146> | **Cog not loaded: `{extension}`**")
    else:
        await ctx.send(f"<:tick:700041815327506532> | **Unloaded Cog: `{extension}`**")

@bot.command(description="Owner only.")
@commands.is_owner()
async def r(ctx):
    """
    Reloads all cogs.
    """
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

@bot.command(description="Owner only.")
@commands.is_owner()
async def cogs(ctx):
    """
    Shows all cogs.
    """
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await ctx.send(f"`{filename[:-3]}`")

# con.close()
# with open('data/token.json', 'r') as f:
#     data = json.load(f)
# bot.run(f'{data["TOKEN"]}')
bot.run('NzAwMDIxNjc3Mjg2ODgzNDQ4.XrKj9A.qTyFu8JGZKqg9hQ5D7--vX715pY')
