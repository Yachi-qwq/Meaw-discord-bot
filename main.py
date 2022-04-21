# MeaMeaw
# shippo discord bot on top.gg = https://top.gg/bot/933735281767612496
from cgitb import text
from imp import source_from_cache
from importlib.resources import contents
from itertools import count
from optparse import Option
from pydoc import describe
from tkinter import END
from tokenize import cookie_re
import youtube_dl
from unicodedata import name
import discord
from discord import message
from discord.ext import commands
import datetime
import os
from discord.utils import get
from discord.ext.commands import has_permissions
import time
import random
from discord.ext import commands
from datetime import datetime
import aiohttp
from discord.ext.commands import has_permissions, MissingPermissions
import aiofiles
from imp import source_from_cache
#from discord_components import DiscordComponents, Button


#bot = 
TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
intetns_all = discord.Intents.all()
#intents = discord.Intents(messages=True, guilds=True, members=True, presence=True)
bot = commands.Bot(command_prefix=commands.when_mentioned_or('-'),  description='online to help', intents = intetns_all, case_insensitive=True) 
#bot.remove_command("help")
bot.warnings = {} #guild_id : {member_id: [count, [(admin_id, reason)]]}
bot.remove_command("help")


# connecion
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("(=^･ｪ･^=)"))
    for guild in bot.guilds:
        async with aiofiles.open(f"{guild.id}.txt", mode="a") as temp:
            pass

        bot.warnings[guild.id] = {}

    for guild in bot.guilds:
        async with aiofiles.open(f"{guild.id}.txt", mode="r") as file:
            lines = await file.readlines()

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                reason = " ".join(data[2:]).strip("\n")

                try:
                    bot.warnings[guild.id][member_id][0] += 1
                    bot.warnings[guild.id][member_id][1].append((admin_id, reason))

                except KeyError:
                    bot.warnings[guild.id][member_id] = [1, [(admin_id, reason)]]

    print(f'  {bot.user.name} is online and connected')
    print(f"  {bot.user.name} is now awake to help her master")
    print("----------------------------------------------------------------------------------------------------------------------")


#speak command
@bot.command(brief='Writes for you text msgs', description='yeah well i think the short version should be clear')
async def speak(ctx, *, text):
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")

#clear
@bot.command(brief='deletes msgs in the range of the number you added', description='yeah well i think the short version should be clear')
@commands.has_permissions(administrator=True, manage_messages = True)
async def clear(ctx, amount: int = 0):
    message = ctx.message
    await message.delete()
    time.sleep(0.02)
    await ctx.channel.purge(limit = amount)


#turn bot offline
@bot.command(brief='turns bot off', description="please don't use this or me (Yachi) will kill you")
@commands.has_permissions(administrator=True)
async def sleep(ctx):
    await ctx.send(f"{bot.user.name} was brought to bed by his master")
    time.sleep(2)
    await bot.close()
    print(f'{bot.user.name} ------------------------------------------------------------- was brought to bed by his master {ctx.author.name} ------------------------------------------------------------- ')

#dm
@bot.command(brief='writes a dm', description='yeah well i think the short version should be clear')
async def dm(ctx, user: discord.User=None, *, msg=None):
    if msg == None:
        await ctx.send(':x: Baka you cant send empty messages')
        await ctx.message.delete()
    if user is None:
        await ctx.send(':x: please add a user')
    else:
        await user.send(msg)
        await ctx.send(f':white_check_mark: message was sent UwU')
        await ctx.message.delete()

#connect to voice channel
@bot.command(brief='joins your voice channel', description='yeah well i think the short version should be clear')
async def join(ctx):
    #channel = ctx.author.voice.channel
    voice_channel = ctx.message.author.voice.channel if ctx.message.author.voice else None
    try:
        if voice_channel is None:
            await ctx.send(":x: Please join a channel and try again")

        elif voice_channel is voice_channel:
            await voice_channel.connect()
            await ctx.reply(f"✅ {bot.user.name} is connected to you voice channel")
        else:
            await ctx.reply(f":x: something went wrong")
            print("something went wrong")
    except AttributeError:
        print("Error with joining voice channel")
        return

    

@bot.command(brief='leaves your yoice channel', description='yeah well i think the short version should be clear') # leavevoice channel
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await ctx.reply(f"✅ {bot.user.name} has left voice channel let's meet soon again")
    #message = ctx.author.message
    #await message.add_reaction('✅')
    #await ctx.send(f"{bot.name} has left voice")

#avatar
@bot.command(brief='shows user avatar', description='yeah well i think the short version should be clear')
async def avatar(ctx, user1 : discord.Member=None):
    if user1 is None:
        await ctx.send(':x: please add a user')
    else:
        user1AvatarUrl = user1.avatar.url
        await ctx.send(user1AvatarUrl)

#userinfo
@bot.command(brief='shows infos about the user', description='yeah well i think the short version should be clear')
async def userinfo(ctx, *, user: discord.Member = None):
    if user is None:
        user = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(color=0xdfa3ff)
        embed.set_author(name=str(user), icon_url=user.avatar.url)
        embed.set_thumbnail(url=user.avatar.url)
        embed.add_field(name="🕰️ Joined", value=user.joined_at.strftime(date_format), inline=False)
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name="🕰️ Registered", value=user.created_at.strftime(date_format), inline=False)
        embed.set_footer(text='ID: ' + str(user.id))
        await ctx.send(embed=embed)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(color=0xdfa3ff)
        embed.set_author(name=str(user), icon_url=user.avatar.url)
        embed.set_thumbnail(url=user.avatar.url)
        embed.add_field(name="🕰️ Joined", value=user.joined_at.strftime(date_format), inline=False)
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name="🕰️ Registered", value=user.created_at.strftime(date_format), inline=False)
        embed.set_footer(text='ID: ' + str(user.id))
        await ctx.send(embed=embed)

#serverinfo
@bot.command(brief='shows infos about the server', description='yeah well i think the short version should be clear')
async def serverinfo(ctx):
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    #region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon.url)

    embed = discord.Embed(
        title=name,
        description=description,
        color=0xf1c40f
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    #embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    embed.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y at %H:%M:%S'), inline=False)
    embed.add_field(name='Bots:', value=(', '.join(list_of_bots)))

    await ctx.send(embed=embed)

#ban
@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):   
        ban = discord.Embed(title=f":boom: Banned {user.name}!, fuck you xD", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await user.send(embed=ban)
        await ctx.channel.send(embed=ban)
        await user.ban(reason=reason)

#lock
bad_words = ['https://www.youtube.com/channel/', 'https://discord.gg/', 'nigger', 'neger']
@bot.event
async def on_message(msg):
    try:
        for word in bad_words:
            if word in msg.content:
                await msg.delete()
                message = "❌not allowed"
                await msg.channel.send(message, delete_after=8)
                await msg.message.delete(delay=8)
        await bot.process_commands(msg)
    except AttributeError:
        return

#add bad word
#liste = [] # leere Liste anlegen
#liste.append(1) # Elemente hinzufügens
#liste.append(3)
#print liste.pop() # und wieder lesen -> 3, 1  
#print liste.pop()
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def addbadword(ctx, *, neww=None):
    bad_words.append(neww)
    msg = ctx.message
    await msg.delete()
    await ctx.send("✅ Bad word is added to list")

        
#unban
#mute
#remove role
@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True, administrator=True)
async def delrole(ctx, member: discord.Member, *, role_name=None):
    try:
        await member.remove_roles(role_name)
    except:
        await ctx.send(f"cannot remove {role_name}")

#vkick
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def vkick(ctx, user: discord.Member=None):
    if user is None:
        await ctx.send("> ❌please add a user")
    else:
        await user.move_to(None)
        await ctx.send(f" {user.mention} you got disconnected from voice")

#mute voice
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def vmute(ctx, user: discord.Member=None):
    if user is None:
        await ctx.send("> ❌please add a user")
    else:
        await user.edit(mute = True)
        await ctx.send(f"> {user.mention} you got muted by {ctx.author.mention}")

#unmute voice
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def vunmute(ctx, user: discord.Member=None):
    if user is None:
        await ctx.send("> ❌please add a user")
    else:
        await user.edit(mute = False)
        await ctx.send(f"> {user.mention} you got unmuted by {ctx.author.mention}")


#kick
@bot.command(name="kick", pass_context=True)
@commands.has_permissions(manage_roles=True, ban_members=True, administrator=True)
async def kick(ctx, user:discord.Member, *, reason="❌ No reason provided"):
        kick = discord.Embed(title=f" ✅ Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)
        await user.kick(reason=reason)

#setnick
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True, manage_nicknames=True, change_nickname=True)
async def setnick(ctx, user: discord.Member=None, nick=None):
    if nick is None:
        await ctx.send("> ❌ please provide a nickname")
    if user is None:
        await ctx.send("> ❌ please provide a user")
    else:
        await user.edit(nick=nick)
        await ctx.send(f"> ✅ {ctx.author.mention} changed nickname for {user.mention}")
    

#warning system
@bot.event
async def on_guild_join(guild):
    bot.warnings[guild.id] = {}

@bot.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member: discord.Member=None, *, reason=None):
    if member is None:
        return await ctx.send("> ❌ The provided member couldn't be found or you forgot to provide one")

    if reason is None:
        return await ctx.send("> ❌ Please provide a reason for the warning")

    try:
        first_warning = False
        bot.warnings[ctx.guild.id][member.id][0] += 1
        bot.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

    except KeyError:
        first_warning = True
        bot.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

    count = bot.warnings[ctx.guild.id][member.id][0]

    async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
        await file.write(f"{member.id} {ctx.author.id} {reason}\n")

    await ctx.send(f"{member.mention} has {count} {'warning' if first_warning else 'warnings'}.")

@bot.command() #shows how ma
@commands.has_permissions(administrator=True)
async def warnings(ctx, member: discord.Member=None, *, reason=None):
    if member is None:
        return await ctx.send("> ❌ The provided member couldn't be found or you forgot to provide one")

    embed = discord.Embed(title=f"Displaying Warnings for {member.name}", description="", color=discord.Color.red())
    try:
        i = 1
        for admin_id, reason in bot.warnings[ctx.guild.id][member.id][1]:
            admin = ctx.guild.get_member(admin_id)
            embed.description += f"**Warnings {i}** given by: {admin.mention} for: *'{reason}'*.\n"
            i += 1

        await ctx.send(embed=embed)
        #os.system(f'start echo {i}')

    except KeyError: #no warnings
        await ctx.send("❌This user has no warnings")

#only fun command
@bot.command(pass_context=True, alias=["Neko"])
async def neko(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/Kemonomimi/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

#create role
@bot.command() #working
async def crole(ctx, name_role=None):
    guild = ctx.guild
    if get(ctx.guild.roles, name=name_role):
        await ctx.send("> role already exists")
    else:
        if name is None:
            await ctx.send("> :x: please add a name for the role")
        else:
            await guild.create_role(name=name_role, color=discord.Colour(0xffffff))
            await ctx.send(f"> ✅ {name} was created")

#add role 
@bot.command()
async def addrole(ctx, user: discord.Member=None, *, role_name=None):
    if user is None:
        await ctx.send("> ❌ please provide a user")
    elif role_name is None:
        await ctx.send("> ❌ please provide a role name")
    else:
        await user.add_roles(discord.utils.get(user.guild.roles, name=role_name))
        await ctx.send(f"> ✅ role was added to {user.mention}")

#buttons
random_number = str(random.randint(0, 7))
class Buttons(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="random number", style=discord.ButtonStyle.red)
    async def red_button(self, button: discord.ui.Button, interaction: discord.Integration):
        await interaction.response.edit_message(content=random_number)
        
@bot.command()
async def button(ctx):
    await ctx.send("press the button to make a random number between 0 and 7", view=Buttons())

#ticket system 
@bot.command()
async def ticket(ctx, *, reason = None):
    guild = ctx.guild
    user = ctx.author
    await ctx.message.delete()
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
    }
    channel = await guild.create_text_channel(f"Ticket from {user}", overwrites=overwrites)
    await channel.send(f"{user.mention}")
    embed = discord.Embed(title=f"{user}  needs some help", description="", color=0xdfa3ff)
    embed.add_field(name="reason", value=f"``{reason}``")
    embed.set_footer(text="please be patient an Admin or Mod will take care of it right away")
    await channel.send(embed=embed)


class help_Button(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="see commands", style=discord.ButtonStyle.red)
    async def red_button(self, button: discord.ui.Button, interaction: discord.Integration):
        await interaction.response.edit_message(content="still in progress")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title = "🍁 Need help? 🍁", description="❗make shure that you put the `Kuso` role on top to use moderation commands❗")
    #embed.title = "🍁 Need help? 🍁"
    embed.add_field(name="⌫ Website", value="[all infos about commands you can find here](https://kuso-bot.mx177013.repl.co/index.html)", inline=False)
    embed.add_field(name="⌫ Invite bot to your server", value="[click to invite](https://discord.com/api/oauth2/authorize?client_id=958473430276132976&permissions=8&scope=bot)", inline=False)
    embed.add_field(name="⌫ Join our Discord server", value="[click to join](https://discord.gg/ZgYRqPRdBB)", inline=False)
    embed.add_field(name="⌫ Join our partner server", value="[click to join](https://discord.gg/9SEaUyCV)", inline=False)
    #embed.add_field(name="⌫ Support number", value="+43 680 2222034", inline=False)
    #embed.add_field(value="**neko** `!neko` sends a neko pic")
    await ctx.reply(embed=embed, view=help_Button())

#google search
@bot.command()
async def search(ctx, *, x=None):
    try:
        from googlesearch import search
        if x is None:
            await ctx.send("> ❌ Please enter something you want to search for")
        else:
            await ctx.send("This could take a moment, thank you for your patience qwq")
            for j in search(x, tld="co.in", num=1, stop=1, pause=2):
                embed = discord.Embed(title="Google search", description=f"here is what i found to {x}:")
                embed.add_field(name="Link: ", value=f"{j}")
                await ctx.send(embed=embed) #Here here is something from google i found to `{x}`:  " + j
    except ImportError:
        await ctx.send("> ❌ Mudule Error please contact the creator")

#wikipedia
#https://de.wikipedia.org/wiki/Tiger
@bot.command(pass_context=True)
async def wiki(ctx, inhalt=None, *, zeilen=None):
    try:
        import wikipedia
        if inhalt is None:
            await ctx.send("> ❌ Please enter something you want to search for")
        elif zeilen is None:
            await ctx.send(f"> ❌ Please enter the amount of sentences you want to read about `{inhalt}`")
        else:
            wikipedia.set_lang("de")
            result = wikipedia.summary(inhalt, sentences = zeilen)
            #embed = discord.Embed(title="__Wikipedia search__", description=f"Here is what I found on Wikipedia.org to {inhalt}")
            #embed.add_field(name=f"{inhalt}: ", value=result)
            await ctx.send(f">>> __**Here is what i found to {inhalt}: **__  {result}")
    except ImportError:
        await ctx.send("> ❌ Mudule Error please contact the creator")

#select menu
class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Option 1",emoji="🔴",description="dings 1"),
            discord.SelectOption(label="Option 2",emoji="🟡",description="dings 2"),
            discord.SelectOption(label="Option 3",emoji="🟢",description="dings 3")
            ]
        super().__init__(placeholder="Dings auswählen",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Option 1":
            await interaction.response.edit_message(content="lets go option 1")
        elif self.values[0] == "Option 2":
            await interaction.response.send_message("dings 2 yes sir",ephemeral=False)
        elif self.values[0] == "Option 3":
            await interaction.response.send_message("3. ding funtioniert",ephemeral=True)

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())

@bot.command()
async def menu(ctx):
    await ctx.send("Menus!",view=SelectView())


#qr code generator
@bot.command()
async def qr(ctx, *, pic=None):
    if pic is None:
        await ctx.send("> ❌ please add text or a link")
    else:
        import qrcode
        img = qrcode.make(f"{pic}")
        img.save(f"{pic}.jpg")
        await ctx.send(file=discord.File(f"{pic}.jpg"))
        time.sleep(5)
        os.remove(f"{pic}.jpg")


bot.run(TOKEN)
# (=^･ｪ･^=) 
