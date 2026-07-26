import discord
from discord.ext import commands
import random
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

token = os.environ["TOKEN"]

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# --- ON READY ---
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over the server | !help"))
    print(f"Bot is online as {bot.user}")

# --- CUSTOM HELP ---
@bot.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(
        title="__XERO BOT__",
        description=(
            "Your all-in-one Discord bot.\n"
            "Use `!help <command>` for more info.\n\n"
            "**Categories**"
        ),
        color=0x2f3136
    )
    embed.set_thumbnail(url=ctx.bot.user.display_avatar.url)
    embed.set_image(url="https://i.imgur.com/6BkCq2E.png")
    embed.add_field(name="__MODERATION__", value="```ban, kick, unban, mute, unmute, warn, slowmode, clear, lock, unlock```", inline=False)
    embed.add_field(name="__FUN__", value="```8ball, coinflip, dice, poll, say```", inline=False)
    embed.add_field(name="__UTILITY__", value="```userinfo, serverinfo, membercount, avatar, remind, calc, ping, hello```", inline=False)
    embed.add_field(name="__ROLES__", value="```giverole, removerole```", inline=False)
    embed.add_field(name="__ADMIN__", value="```announce, giveaway```", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=embed)

@help.command()
async def ban(ctx):
    embed = discord.Embed(title="BAN", description="Ban a member from the server", color=0xed4245)
    embed.add_field(name="Usage", value="`!ban @user reason`", inline=False)
    embed.add_field(name="Permission", value="Ban Members", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def kick(ctx):
    embed = discord.Embed(title="KICK", description="Kick a member from the server", color=0xed4245)
    embed.add_field(name="Usage", value="`!kick @user reason`", inline=False)
    embed.add_field(name="Permission", value="Kick Members", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def unban(ctx):
    embed = discord.Embed(title="UNBAN", description="Unban a user by username", color=0xed4245)
    embed.add_field(name="Usage", value="`!unban username`", inline=False)
    embed.add_field(name="Permission", value="Ban Members", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def mute(ctx):
    embed = discord.Embed(title="MUTE", description="Timeout a member", color=0xfea611)
    embed.add_field(name="Usage", value="`!mute @user minutes`", inline=False)
    embed.add_field(name="Permission", value="Moderate Members", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def unmute(ctx):
    embed = discord.Embed(title="UNMUTE", description="Remove timeout from a member", color=0xfea611)
    embed.add_field(name="Usage", value="`!unmute @user`", inline=False)
    embed.add_field(name="Permission", value="Moderate Members", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def warn(ctx):
    embed = discord.Embed(title="WARN", description="Warn a member", color=0xfea611)
    embed.add_field(name="Usage", value="`!warn @user reason`", inline=False)
    embed.add_field(name="Permission", value="Manage Messages", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def slowmode(ctx):
    embed = discord.Embed(title="SLOWMODE", description="Set channel slowmode", color=0xfea611)
    embed.add_field(name="Usage", value="`!slowmode seconds`", inline=False)
    embed.add_field(name="Permission", value="Manage Messages", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def clear(ctx):
    embed = discord.Embed(title="CLEAR", description="Bulk delete messages", color=0xfea611)
    embed.add_field(name="Usage", value="`!clear amount`", inline=False)
    embed.add_field(name="Permission", value="Manage Messages", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def lock(ctx):
    embed = discord.Embed(title="LOCK", description="Lock the current channel", color=0xfea611)
    embed.add_field(name="Usage", value="`!lock`", inline=False)
    embed.add_field(name="Permission", value="Manage Channels", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def unlock(ctx):
    embed = discord.Embed(title="UNLOCK", description="Unlock the current channel", color=0xfea611)
    embed.add_field(name="Usage", value="`!unlock`", inline=False)
    embed.add_field(name="Permission", value="Manage Channels", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command(name="8ball")
async def eight_ball(ctx):
    embed = discord.Embed(title="8BALL", description="Ask the magic 8ball a question", color=0x9b59b6)
    embed.add_field(name="Usage", value="`!8ball question`", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def coinflip(ctx):
    embed = discord.Embed(title="COINFLIP", description="Flip a coin", color=0x9b59b6)
    embed.add_field(name="Usage", value="`!coinflip`", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def dice(ctx):
    embed = discord.Embed(title="DICE", description="Roll a dice", color=0x9b59b6)
    embed.add_field(name="Usage", value="`!dice`", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def poll(ctx):
    embed = discord.Embed(title="POLL", description="Create a yes/no poll", color=0x9b59b6)
    embed.add_field(name="Usage", value="`!poll question`", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def say(ctx):
    embed = discord.Embed(title="SAY", description="Make the bot say something", color=0x9b59b6)
    embed.add_field(name="Usage", value="`!say message`", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def userinfo(ctx):
    embed = discord.Embed(title="USERINFO", description="Get info about a member", color=0x57f287)
    embed.add_field(name="Usage", value="`!userinfo @user`", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def serverinfo(ctx):
    embed = discord.Embed(title="SERVERINFO", description="Get info about the server", color=0x57f287)
    embed.add_field(name="Usage", value="`!serverinfo`", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def membercount(ctx):
    embed = discord.Embed(title="MEMBERCOUNT", description="Get the member count", color=0x57f287)
    embed.add_field(name="Usage", value="`!membercount`", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def avatar(ctx):
    embed = discord.Embed(title="AVATAR", description="Get a member's avatar", color=0x57f287)
    embed.add_field(name="Usage", value="`!avatar @user`", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def remind(ctx):
    embed = discord.Embed(title="REMIND", description="Set a reminder", color=0x57f287)
    embed.add_field(name="Usage", value="`!remind minutes message`", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def calc(ctx):
    embed = discord.Embed(title="CALC", description="Calculate math", color=0x57f287)
    embed.add_field(name="Usage", value="`!calc 2+2`", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def ping(ctx):
    embed = discord.Embed(title="PING", description="Check bot latency", color=0x57f287)
    embed.add_field(name="Usage", value="`!ping`", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def hello(ctx):
    embed = discord.Embed(title="HELLO", description="Say hello to the bot", color=0x57f287)
    embed.add_field(name="Usage", value="`!hello`", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def giverole(ctx):
    embed = discord.Embed(title="GIVEROLE", description="Give a role to a member", color=0x57f287)
    embed.add_field(name="Usage", value="`!giverole @user @role`", inline=False)
    embed.add_field(name="Permission", value="Manage Roles", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def removerole(ctx):
    embed = discord.Embed(title="REMOVEROLE", description="Remove a role from a member", color=0x57f287)
    embed.add_field(name="Usage", value="`!removerole @user @role`", inline=False)
    embed.add_field(name="Permission", value="Manage Roles", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def announce(ctx):
    embed = discord.Embed(title="ANNOUNCE", description="Send an announcement embed", color=0xfee75c)
    embed.add_field(name="Usage", value="`!announce message`", inline=False)
    embed.add_field(name="Permission", value="Manage Messages", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

@help.command()
async def giveaway(ctx):
    embed = discord.Embed(title="GIVEAWAY", description="Start a giveaway", color=0xfee75c)
    embed.add_field(name="Usage", value="`!giveaway seconds prize`", inline=False)
    embed.add_field(name="Example", value="`!giveaway 60 Nitro`", inline=False)
    embed.add_field(name="Permission", value="Manage Messages", inline=False)
    embed.set_footer(text="Xero Bot")
    await ctx.send(embed=embed)

# --- WELCOME MESSAGE ---
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    embed = discord.Embed(
        title=f"Welcome to {member.guild.name}!",
        description=f"Hey {member.mention}, enjoy your stay!\nYou are member **#{member.guild.member_count}**",
        color=0x57f287
    )
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.set_image(url="https://i.imgur.com/6BkCq2E.png")
    embed.set_footer(text=f"Joined {member.guild.name}", icon_url=member.guild.icon.url if member.guild.icon else None)
    await channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    embed = discord.Embed(
        title="Goodbye!",
        description=f"**{member.name}** has left the server.",
        color=0xed4245
    )
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.set_footer(text=f"Members: {member.guild.member_count}")
    await channel.send(embed=embed)

# --- MODERATION ---
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason"):
    embed = discord.Embed(title="BANNED", description=f"{member.mention} has been banned", color=0xed4245)
    embed.add_field(name="Reason", value=reason, inline=False)
    embed.set_thumbnail(url=member.display_avatar.url)
    await ctx.send(embed=embed)
    await member.ban(reason=reason)

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member_name):
    banned = [entry async for entry in ctx.guild.bans()]
    for ban_entry in banned:
        if ban_entry.user.name == member_name:
            await ctx.guild.unban(ban_entry.user)
            embed = discord.Embed(title="UNBANNED", description=f"**{ban_entry.user}** has been unbanned", color=0x57f287)
            await ctx.send(embed=embed)
            return

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason"):
    embed = discord.Embed(title="KICKED", description=f"{member.mention} has been kicked", color=0xfea611)
    embed.add_field(name="Reason", value=reason, inline=False)
    embed.set_thumbnail(url=member.display_avatar.url)
    await ctx.send(embed=embed)
    await member.kick(reason=reason)

@bot.command()
@commands.has_permissions(moderate_members=True)
async def mute(ctx, member: discord.Member, minutes: int = 10):
    await member.timeout(discord.utils.utcnow() + discord.timedelta(minutes=minutes))
    embed = discord.Embed(title="MUTED", description=f"{member.mention} has been muted for **{minutes} minutes**", color=0xfea611)
    embed.set_thumbnail(url=member.display_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(moderate_members=True)
async def unmute(ctx, member: discord.Member):
    await member.timeout(None)
    embed = discord.Embed(title="UNMUTED", description=f"{member.mention} has been unmuted", color=0x57f287)
    embed.set_thumbnail(url=member.display_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member: discord.Member, *, reason="No reason"):
    embed = discord.Embed(title="WARNING", description=f"{member.mention} has been warned", color=0xfea611)
    embed.add_field(name="Reason", value=reason, inline=False)
    embed.set_thumbnail(url=member.display_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def slowmode(ctx, seconds: int = 0):
    await ctx.channel.edit(slowmode_delay=seconds)
    embed = discord.Embed(title="SLOWMODE", description=f"Slowmode set to **{seconds} seconds**", color=0x57f287)
    await ctx.send(embed=embed)

# --- FUN ---
@bot.command(name="8ball")
async def eight_ball(ctx, *, question):
    responses = ["Yes", "No", "Maybe", "Ask again later", "Definitely", "Absolutely not", "Most likely", "Doubtful"]
    embed = discord.Embed(title="8BALL", color=0x9b59b6)
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=random.choice(responses), inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def coinflip(ctx):
    result = random.choice(["Heads", "Tails"])
    embed = discord.Embed(title="COINFLIP", description=f"**{result}!**", color=0x9b59b6)
    await ctx.send(embed=embed)

@bot.command()
async def dice(ctx):
    result = random.randint(1, 6)
    embed = discord.Embed(title="DICE", description=f"You rolled a **{result}**", color=0x9b59b6)
    await ctx.send(embed=embed)

@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="POLL", description=question, color=0x9b59b6)
    embed.set_footer(text=f"Poll by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")

@bot.command()
async def say(ctx, *, message):
    embed = discord.Embed(description=message, color=0x9b59b6)
    await ctx.send(embed=embed)

# --- UTILITY ---
@bot.command()
async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(title=member.display_name, color=0x57f287)
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.add_field(name="Joined", value=f"<t:{int(member.joined_at.timestamp())}:R>", inline=True)
    embed.add_field(name="Account Created", value=f"<t:{int(member.created_at.timestamp())}:R>", inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    roles = [role.mention for role in member.roles[1:]]
    embed.add_field(name=f"Roles [{len(roles)}]", value=" ".join(roles) if roles else "None", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def membercount(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", color=0x57f287)
    embed.add_field(name="Total Members", value=ctx.guild.member_count, inline=True)
    embed.add_field(name="Humans", value=sum(1 for m in ctx.guild.members if not m.bot), inline=True)
    embed.add_field(name="Bots", value=sum(1 for m in ctx.guild.members if m.bot), inline=True)
    if ctx.guild.icon:
        embed.set_thumbnail(url=ctx.guild.icon.url)
    await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    embed = discord.Embed(title=guild.name, color=0x57f287)
    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)
    embed.add_field(name="Owner", value=guild.owner.mention, inline=True)
    embed.add_field(name="Members", value=guild.member_count, inline=True)
    embed.add_field(name="Channels", value=len(guild.channels), inline=True)
    embed.add_field(name="Roles", value=len(guild.roles), inline=True)
    embed.add_field(name="Emojis", value=len(guild.emojis), inline=True)
    embed.add_field(name="Boosts", value=guild.premium_subscription_count, inline=True)
    embed.add_field(name="Created", value=f"<t:{int(guild.created_at.timestamp())}:R>", inline=True)
    embed.add_field(name="Verification Level", value=str(guild.verification_level).title(), inline=True)
    embed.set_footer(text=f"ID: {guild.id}")
    await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"{member.display_name}'s Avatar", color=0x57f287)
    embed.set_image(url=member.display_avatar.url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def remind(ctx, minutes: int, *, message):
    embed = discord.Embed(title="REMINDER SET", description=f"I'll remind you in **{minutes} minutes**\n> {message}", color=0x57f287)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=embed)
    await asyncio.sleep(minutes * 60)
    await ctx.author.send(f"⏰ Reminder: **{message}**")

@bot.command()
async def calc(ctx, *, expression):
    try:
        result = eval(expression)
        embed = discord.Embed(title="CALCULATOR", color=0x57f287)
        embed.add_field(name="Expression", value=f"`{expression}`", inline=False)
        embed.add_field(name="Result", value=f"**{result}**", inline=False)
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(title="ERROR", description="Invalid math expression", color=0xed4245)
        await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    embed = discord.Embed(title="PONG!", description=f"Latency: **{round(bot.latency * 1000)}ms**", color=0x57f287)
    await ctx.send(embed=embed)

@bot.command()
async def hello(ctx):
    embed = discord.Embed(description=f"Hello {ctx.author.mention}!", color=0x57f287)
    embed.set_thumbnail(url=ctx.bot.user.display_avatar.url)
    await ctx.send(embed=embed)

# --- ADMIN ---
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    deleted = await ctx.channel.purge(limit=amount + 1)
    embed = discord.Embed(title="CLEARED", description=f"Deleted **{len(deleted) - 1}** messages", color=0x57f287)
    await ctx.send(embed=embed, delete_after=3)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    embed = discord.Embed(title="CHANNEL LOCKED", description="This channel has been locked", color=0xed4245)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    embed = discord.Embed(title="CHANNEL UNLOCKED", description="This channel has been unlocked", color=0x57f287)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def announce(ctx, *, message):
    embed = discord.Embed(title="ANNOUNCEMENT", description=message, color=0xfee75c)
    embed.set_footer(text=f"Announced by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=embed)

# --- ROLES ---
@bot.command()
@commands.has_permissions(manage_roles=True)
async def giverole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    embed = discord.Embed(title="ROLE GIVEN", description=f"Added {role.mention} to {member.mention}", color=0x57f287)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    embed = discord.Embed(title="ROLE REMOVED", description=f"Removed {role.mention} from {member.mention}", color=0xfea611)
    await ctx.send(embed=embed)

# --- GIVEAWAY ---
@bot.command()
@commands.has_permissions(manage_messages=True)
async def giveaway(ctx, time: int, *, prize):
    embed = discord.Embed(title="GIVEAWAY!", description=f"Prize: **{prize}**\nReact with 🎉 to enter!\nEnds in **{time} seconds**", color=0xfee75c)
    embed.set_footer(text=f"Started by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("🎉")
    await asyncio.sleep(time)
    new_msg = await ctx.channel.fetch_message(msg.id)
    users = [user async for user in new_msg.reactions[0].users() if not user.bot]
    if users:
        winner = random.choice(users)
        embed = discord.Embed(title="GIVEAWAY ENDED", description=f"🎉 {winner.mention} won **{prize}**!", color=0xfee75c)
        embed.set_thumbnail(url=winner.display_avatar.url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="GIVEAWAY ENDED", description="No one entered the giveaway", color=0xed4245)
        await ctx.send(embed=embed)

bot.run(token)
