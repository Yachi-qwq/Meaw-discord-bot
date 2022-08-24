import discord
from discord import Forbidden, message
from discord.ext import commands
import os
import time
import random
from discord.ext import commands
from datetime import datetime
#for reddit cmds
import aiohttp 
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get

#commands line thing
intetns = discord.Intents.all()
bot = commands.Bot(bot = commands.Bot(command_prefix=commands.when_mentioned_or('.?')),  description='just online', intents = intetns)

#bot token
TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# connecion
@bot.event
async def on_ready():

    print("""

     ▄█▀▀▀█▄███         ██
    ▄██    ▀███
    ▀███▄    ███████▄ ▀███ ▀████████▄▀████████▄  ▄██▀██▄
      ▀█████▄██    ██   ██   ██   ▀██  ██   ▀██ ██▀   ▀██
    ▄     ▀████    ██   ██   ██    ██  ██    ██ ██     ██
    ██     ████    ██   ██   ██   ▄██  ██   ▄██ ██▄   ▄██
    █▀█████▀████  ████▄████▄ ██████▀   ██████▀   ▀█████▀
                             ██        ██
                            ▄████▄    ▄████▄
    """)
    print(f' ✅ {bot.user.name} is online and connected')
    print(f" ✅ {bot.user.name} is now awake to help her master")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("Einladungslink =         https://discord.com/api/oauth2/authorize?client_id=933735281767612496&permissions=8&scope=bot")
    print("started with Token:  " + TOKEN)

####################### THINGS
#disconnect bot
@bot.command(alias=["quit"])
@commands.has_permissions(administrator=True)
async def sleep(ctx):
    await ctx.send(f"{bot.user.name} was brought to bed by his master")
    time.sleep(2)
    await bot.close()
    print(f'{bot.user.name} ------------------------------------------------------------- was brought to bed by this master Yachi ------------------------------------------------------------- ')


####################### MODERATION
#lock
bad_words = ['word1', 'word2', 'word3', 'word4', 'word5']
@bot.event
async def on_message(msg):
    try:
        for word in bad_words:
            if word in msg.content:
                await msg.delete()
                message = "❌not allowed"
                await msg.channel.send(message, delete_after=8)
                await msg.message.delete(delay=44)
        await bot.process_commands(msg)
    except AttributeError:
        return

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def addbadword(ctx, *, neww=None):
    if neww is None:
        await ctx.send("❌please add a word")
    else:
        bad_words.append(neww)
        msg = ctx.message
        await msg.delete()
        await ctx.send("✅ Bad word is added to list")


#userinfo
@bot.command(brief='shows infos about the user', description='yeah well i think the short version should be clear')
async def userinfo(ctx, *, user: discord.Member = None):
    if user is None:
        user = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(color=0xdfa3ff, title="**USER INFO**", description=f"**User ID:** {user.id}")
        embed.add_field(name="** **", value="** **", inline=False)
        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name=":clock: Join and creation time", value=f"**Joined server:** {user.joined_at.strftime(date_format)}\n**Account created:** {user.created_at.strftime(date_format)}", inline=False)
        embed.add_field(name="** **", value="** **", inline=False)
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name=":hourglass: Join position:", value=f"your join position is: **{str(members.index(user)+1)}**", inline=False)

        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])

        embed.add_field(name="** **", value="** **", inline=False)
        embed.add_field(name=":scroll: Your roles: [{}]".format(len(user.roles)-1), value=role_string, inline=False)
        embed.add_field(name="** **", value="** **", inline=False)

        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        embed.add_field(name=":no_entry: Server permissions", value=perm_string, inline=False)

        embed.set_footer(text='userinfo')
        await ctx.send(embed=embed)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(color=0xdfa3ff, title="**USER INFO**", description=f"**User ID:** {user.id}")
        embed.add_field(name="** **", value="** **", inline=False)
        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name=":clock: Join and creation time", value=f"**Joined server:** {user.joined_at.strftime(date_format)}\n**Account created:** {user.created_at.strftime(date_format)}", inline=False)
        embed.add_field(name="** **", value="** **", inline=False)
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name=":hourglass: Join position:", value=f"your join position is: **{str(members.index(user)+1)}**", inline=False)

        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])

        embed.add_field(name="** **", value="** **", inline=False)
        embed.add_field(name=":scroll: roles: [{}]".format(len(user.roles)-1), value=role_string, inline=False)
        embed.add_field(name="** **", value="** **", inline=False)

        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        embed.add_field(name=":no_entry: Server permissions", value=perm_string, inline=False)

        embed.set_footer(text='userinfo')
        await ctx.send(embed=embed)


#serverinfp
@bot.command(alias = ['si'])
async def serverinfo(ctx):
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    owner = str(ctx.guild.owner.id)
    id = str(ctx.guild.id)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    true_member_count = len([m for m in ctx.guild.members if not m.bot])

    embed = discord.Embed(title=f"**__Server info {name}__**", description=f"- **description:** ```{description}```", color=0xf1c40f)
    embed.set_thumbnail(url=icon)
    embed.add_field(name="** **", 
    value=f"- :crown: **owner:** <@{owner}> ({ctx.guild.owner})\n- :id: **Server ID:** {id}\n- :chart_with_upwards_trend: **Member Count:** {memberCount}\n- :person_standing: **Humans:** {true_member_count}\n- :clock: **Created At:** {ctx.guild.created_at.__format__('%A, %d. %B %Y at %H:%M:%S')}\n- :pencil: **Text channels:** {len(ctx.guild.text_channels)}\n- :loud_sound: **Voice channels:** {len(ctx.guild.voice_channels)}\n- :bar_chart: **Roles:** {len(ctx.guild.roles)}", inline=False)
    embed.add_field(name='Bots:', value=(', '.join(list_of_bots)))
    embed.set_footer(text="serverinfo")
    await ctx.send(embed=embed)





#kick
@bot.command(name="kick", pass_context=True)
@commands.has_permissions(manage_roles=True, ban_members=True)
@commands.has_permissions(administrator=True)
async def kick(ctx, user: discord.Member=None, *, reason=None):
        emoji = discord.utils.get(bot.emojis, name='anime1')
        if user is None:
            await ctx.send(f":x: {ctx.author.name} please provide a user!")
        else:
            if reason is None:
                kick = discord.Embed(title=f" {str(emoji)} __{ctx.author.name}__ kicked __*{user.name}#{user.discriminator}*__", color=0x992d22)
                await ctx.message.delete()
                await ctx.channel.send(embed=kick)
                try:
                    await user.send(embed=kick)
                except:
                    pass
                await user.kick(reason=reason)

            else:
                kick = discord.Embed(title=f" {str(emoji)} __{ctx.author.name}__ kicked __*{user.name}#{user.discriminator}*__ for reason: *{reason}*", color=0x992d22)
                await ctx.message.delete()
                await ctx.channel.send(embed=kick)
                try:
                    await user.send(embed=kick)
                except:
                    pass
                await user.kick(reason=reason)


#ban
@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, user: discord.Member=None, *, reason=None):   #"No reason provided"
        emoji = discord.utils.get(bot.emojis, name='angryawoo')
        if user is None:
            await ctx.send(f"❌ {ctx.author.name} please provide a user")
        else:
            if reason is None:
                ban = discord.Embed(title=f" {str(emoji)} __{ctx.author.name}__ banned __*{user.name}#{user.discriminator}*__", color=0x992d22) #, description=f"Reason: {reason} By: {ctx.author.mention}"
                await ctx.message.delete()
                await ctx.channel.send(embed=ban)
                try:
                    await user.send(embed=ban)
                except:
                    pass
                await user.ban(reason=reason)

            else:
                ban = discord.Embed(title=f" {str(emoji)} __{ctx.author.name}__ banned __*{user.name}#{user.discriminator}*__ for reason: *{reason}*", color=0x992d22) #, description=f"Reason: {reason} By: {ctx.author.mention}"
                await ctx.message.delete()
                await ctx.channel.send(embed=ban)
                try:
                    await user.send(embed=ban)
                except:
                    pass
                await user.ban(reason=reason)



#make chat
@bot.command() #chat
@commands.has_permissions(administrator=True)
async def makechat(ctx, *, name=None):
    guild = ctx.message.guild
    if name == None:
        await ctx.send(' ❌ please add a channel name')
    else:
        await guild.create_text_channel(name)
        await ctx.send(f' ✅ Text channel was created. name = {name}')


#make voice
@bot.command() #voice
async def makevoice(ctx, *, name=None):
    guild = ctx.message.guild
    if name == None:
        await ctx.send(' add a name pls :3 ')

    else:
        embed1 = discord.Embed(
        title = 'Voice creation',
        description = 'React  to create a voice channel.',
        color = 0
    )

    embed1.set_footer(text="By shippo team")

    msg1 = await ctx.send(embed=embed1)
    await msg1.add_reaction("")

    def check(reaction, user):
        return str(reaction) == '' and ctx.author == user

    await bot.wait_for("reaction_add", check=check)
    await guild.create_voice_channel(name=f'{name}') #- {ctx.author}
    await ctx.send(' ✅ Voice channel created ')
    return str(check)


#announcement
allowed_mentions = discord.AllowedMentions(everyone=True)
@bot.command(alias=["event"])
async def announcement(ctx, *, text=None):
    message = ctx.message
    if text is None:
        await ctx.send(" ❌ please add something to say")
    else:
        await message.delete()
        await ctx.send(content = f'@everyone {text}', allowed_mentions = allowed_mentions)


#clear
@bot.command()
@commands.has_permissions(administrator=True, manage_messages = True)
async def clear(ctx, amount: int = 0):
    message = ctx.message
    await message.delete()
    if amount == 0:
        await ctx.send(":x: please add a number")
    else:
        time.sleep(0.02)
        await ctx.channel.purge(limit = amount)


#add role
@bot.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, user: discord.Member=None, *, role_name: discord.Role=None):
    if user is None:
        await ctx.send(" ❌ please provide a user")
    elif role_name is None:
        await ctx.send(" ❌ please provide a role name")
    else:
        try:
            #role = ctx.guild.get_role(role_name)
            #await user.add_roles(discord.utils.get(user.guild.roles, name=role_name))
            await user.add_roles(role_name)
            await ctx.send(f" ✅ {role_name.mention} role was added to {user.mention}")
        except PermissionError:
            await ctx.send(" ❌ I dont have permissions to do that")


#delrole
@bot.command()
@commands.has_permissions(manage_roles=True)
async def delrole(ctx, user: discord.Member=None, *, role_name: discord.Role=None):
    if user is None:
        await ctx.send(" ❌ please provide a user")
    elif role_name is None:
        await ctx.send(" ❌ please provide a role name")
    else:
        try:
            #role = ctx.guild.get_role(role_name)
            #await user.add_roles(discord.utils.get(user.guild.roles, name=role_name))
            await user.remove_roles(role_name)
            await ctx.send(f" ✅ {role_name.mention} role got deleted from {user.mention}")
        except PermissionError:
            await ctx.send(" ❌ I dont have permissions to do that")


#create role
@bot.command() #working
async def crole(ctx, *, name_role=None):
    guild = ctx.guild
    if get(ctx.guild.roles, name=name_role):
        await ctx.send(" role already exists")
    else:
        if name_role is None:
            await ctx.send(" :x: please add a name for the role")
        else:
            await guild.create_role(name=name_role, color="red")
            await ctx.send(f" ✅ {name_role} was created")


#setnick
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True, manage_nicknames=True, change_nickname=True)
async def setnick(ctx, user: discord.Member=None, *, nick=None):
    if nick is None:
        await ctx.send(" ❌ please provide a nickname")
    if user is None:
        await ctx.send(" ❌ please provide a user")
    else:
        await user.edit(nick=nick)
        await ctx.send(f" ✅ {ctx.author.mention} changed nickname for {user.mention}")


#vkick
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def vkick(ctx, user: discord.Member=None):
    if user is None:
        await ctx.send(" ❌please add a user")
    else:
        await user.move_to(None)
        await ctx.send(f" {user.mention} you got disconnected from voice")


#mute voice
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def vmute(ctx, user: discord.Member=None):
    if user is None:
        await ctx.send(" ❌please add a user")
    else:
        await user.edit(mute = True)
        await ctx.send(f":mute: {user.mention} you got muted by {ctx.author.mention}")

#unmute voice
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def vunmute(ctx, user: discord.Member=None):
    if user is None:
        await ctx.send(" ❌please add a user")
    else:
        await user.edit(mute = False)
        await ctx.send(f":loud_sound: {user.mention} you got unmuted by {ctx.author.mention}")


#slowmode
@bot.command()
async def slowmode(ctx, sec: int=None):
    if sec is None:
        await ctx.send(":x: please add the amount of seconds for the slowmode or if you want to turn it off set the seconds to __0__")
    else:
        await ctx.channel.edit(slowmode_delay=sec)
        await ctx.send(f"{ctx.author.mention} set the slowmode delay in this channel to __{sec}__ seconds!")

#lock channel
@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('**:lock: Channel locked.**')

#unlock channel
@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('**:unlock: Channel unlocked.**')

#timeout
@bot.command(pass_context =True)
async def timeout2(ctx, member:discord.User=None, time=None):
    user = await bot.fetch_user(member)
    await user.timeout_for(time)
    await ctx.send (f"{user} callate un rato anda {time}")
