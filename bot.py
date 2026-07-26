import discord
from discord.ext import commands
import random
import asyncio
import os
import platform
import time

token = os.environ["TOKEN"]

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
bot.launch_time = None

EMBED_COLOR = 0x2b2d31
ACCENT = 0x5865f2
SUCCESS = 0x57f287
DANGER = 0xed4245
WARNING = 0xfee75c
PURPLE = 0x9b59b6
BLURPLE = 0x5865f2

def make_embed(title, description="", color=EMBED_COLOR):
    e = discord.Embed(title=title, description=description, color=color)
    return e

# --- ON READY ---
@bot.event
async def on_ready():
    bot.launch_time = time.time()
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"over {len(bot.guilds)} servers | !help"
        )
    )
    print(f"[XERO] Online as {bot.user} | {len(bot.guilds)} guilds | {len(bot.users)} users")

# --- ON COMMAND ERROR ---
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = make_embed("Missing Permissions", f"You need: **{', '.join(error.missing_permissions)}**", DANGER)
        await ctx.send(embed=embed, delete_after=8)
    elif isinstance(error, commands.MemberNotFound):
        embed = make_embed("Member Not Found", "That user doesn't seem to exist.", DANGER)
        await ctx.send(embed=embed, delete_after=8)
    elif isinstance(error, commands.RoleNotFound):
        embed = make_embed("Role Not Found", "That role doesn't seem to exist.", DANGER)
        await ctx.send(embed=embed, delete_after=8)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = make_embed("Missing Argument", f"You forgot: **{error.param.name}**", WARNING)
        await ctx.send(embed=embed, delete_after=8)
    elif isinstance(error, commands.CommandNotFound):
        return
    else:
        embed = make_embed("Error", f"```{str(error)[:1000]}```", DANGER)
        await ctx.send(embed=embed, delete_after=10)

# --- CUSTOM HELP ---
@bot.group(invoke_without_command=True)
async def help(ctx):
    embed = make_embed(
        "XERO BOT",
        "Your all-in-one Discord bot.\nUse `!help <command>` for more info.\n\n**Categories**",
        BLURPLE
    )
    embed.set_thumbnail(url=ctx.bot.user.display_avatar.url)
    embed.set_image(url="https://i.imgur.com/6BkCq2E.png")
    embed.add_field(name="MODERATION", value="```ban · kick · unban · mute · unmute · warn · slowmode · clear · lock · unlock```", inline=False)
    embed.add_field(name="FUN", value="```8ball · coinflip · dice · poll · say```", inline=False)
    embed.add_field(name="UTILITY", value="```userinfo · serverinfo · membercount · avatar · remind · calc · ping · hello```", inline=False)
    embed.add_field(name="ROLES", value="```giverole · removerole```", inline=False)
    embed.add_field(name="ADMIN", value="```announce · giveaway```", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=embed)

@help.command()
async def ban(ctx):
    e = make_embed("BAN", "Ban a member from the server", DANGER)
    e.add_field(name="Usage", value="`!ban @user reason`", inline=False)
    e.add_field(name="Permission", value="Ban Members", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def kick(ctx):
    e = make_embed("KICK", "Kick a member from the server", DANGER)
    e.add_field(name="Usage", value="`!kick @user reason`", inline=False)
    e.add_field(name="Permission", value="Kick Members", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def unban(ctx):
    e = make_embed("UNBAN", "Unban a user by username", DANGER)
    e.add_field(name="Usage", value="`!unban username`", inline=False)
    e.add_field(name="Permission", value="Ban Members", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def mute(ctx):
    e = make_embed("MUTE", "Timeout a member", WARNING)
    e.add_field(name="Usage", value="`!mute @user minutes`", inline=False)
    e.add_field(name="Permission", value="Moderate Members", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def unmute(ctx):
    e = make_embed("UNMUTE", "Remove timeout from a member", WARNING)
    e.add_field(name="Usage", value="`!unmute @user`", inline=False)
    e.add_field(name="Permission", value="Moderate Members", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def warn(ctx):
    e = make_embed("WARN", "Warn a member", WARNING)
    e.add_field(name="Usage", value="`!warn @user reason`", inline=False)
    e.add_field(name="Permission", value="Manage Messages", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def slowmode(ctx):
    e = make_embed("SLOWMODE", "Set channel slowmode", WARNING)
    e.add_field(name="Usage", value="`!slowmode seconds`", inline=False)
    e.add_field(name="Permission", value="Manage Messages", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def clear(ctx):
    e = make_embed("CLEAR", "Bulk delete messages", WARNING)
    e.add_field(name="Usage", value="`!clear amount`", inline=False)
    e.add_field(name="Permission", value="Manage Messages", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def lock(ctx):
    e = make_embed("LOCK", "Lock the current channel", WARNING)
    e.add_field(name="Usage", value="`!lock`", inline=False)
    e.add_field(name="Permission", value="Manage Channels", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def unlock(ctx):
    e = make_embed("UNLOCK", "Unlock the current channel", WARNING)
    e.add_field(name="Usage", value="`!unlock`", inline=False)
    e.add_field(name="Permission", value="Manage Channels", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command(name="8ball")
async def eight_ball(ctx):
    e = make_embed("8BALL", "Ask the magic 8ball a question", PURPLE)
    e.add_field(name="Usage", value="`!8ball question`", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def coinflip(ctx):
    e = make_embed("COINFLIP", "Flip a coin", PURPLE)
    e.add_field(name="Usage", value="`!coinflip`", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def dice(ctx):
    e = make_embed("DICE", "Roll a dice", PURPLE)
    e.add_field(name="Usage", value="`!dice`", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def poll(ctx):
    e = make_embed("POLL", "Create a yes/no poll", PURPLE)
    e.add_field(name="Usage", value="`!poll question`", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def say(ctx):
    e = make_embed("SAY", "Make the bot say something", PURPLE)
    e.add_field(name="Usage", value="`!say message`", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def userinfo(ctx):
    e = make_embed("USERINFO", "Get info about a member", SUCCESS)
    e.add_field(name="Usage", value="`!userinfo @user`", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def serverinfo(ctx):
    e = make_embed("SERVERINFO", "Get info about the server", SUCCESS)
    e.add_field(name="Usage", value="`!serverinfo`", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def membercount(ctx):
    e = make_embed("MEMBERCOUNT", "Get the member count", SUCCESS)
    e.add_field(name="Usage", value="`!membercount`", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def avatar(ctx):
    e = make_embed("AVATAR", "Get a member's avatar", SUCCESS)
    e.add_field(name="Usage", value="`!avatar @user`", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def remind(ctx):
    e = make_embed("REMIND", "Set a reminder", SUCCESS)
    e.add_field(name="Usage", value="`!remind minutes message`", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def calc(ctx):
    e = make_embed("CALC", "Calculate math", SUCCESS)
    e.add_field(name="Usage", value="`!calc 2+2`", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def ping(ctx):
    e = make_embed("PING", "Check bot latency", SUCCESS)
    e.add_field(name="Usage", value="`!ping`", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def hello(ctx):
    e = make_embed("HELLO", "Say hello to the bot", SUCCESS)
    e.add_field(name="Usage", value="`!hello`", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def giverole(ctx):
    e = make_embed("GIVEROLE", "Give a role to a member", SUCCESS)
    e.add_field(name="Usage", value="`!giverole @user @role`", inline=False)
    e.add_field(name="Permission", value="Manage Roles", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def removerole(ctx):
    e = make_embed("REMOVEROLE", "Remove a role from a member", SUCCESS)
    e.add_field(name="Usage", value="`!removerole @user @role`", inline=False)
    e.add_field(name="Permission", value="Manage Roles", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def announce(ctx):
    e = make_embed("ANNOUNCE", "Send an announcement embed", WARNING)
    e.add_field(name="Usage", value="`!announce message`", inline=False)
    e.add_field(name="Permission", value="Manage Messages", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

@help.command()
async def giveaway(ctx):
    e = make_embed("GIVEAWAY", "Start a giveaway", WARNING)
    e.add_field(name="Usage", value="`!giveaway seconds prize`", inline=False)
    e.add_field(name="Example", value="`!giveaway 60 Nitro`", inline=False)
    e.add_field(name="Permission", value="Manage Messages", inline=False)
    e.set_footer(text="Xero Bot")
    await ctx.send(embed=e)

# --- WELCOME / GOODBYE ---
@bot.event
async def on_member_join(member):
    try:
        channel = member.guild.system_channel
        if not channel:
            return
        e = make_embed(
            f"Welcome to {member.guild.name}!",
            f"Hey {member.mention}, enjoy your stay!\nYou are member **#{member.guild.member_count}**",
            SUCCESS
        )
        e.set_thumbnail(url=member.display_avatar.url)
        e.set_image(url="https://i.imgur.com/6BkCq2E.png")
        e.set_footer(
            text=f"Joined {member.guild.name}",
            icon_url=member.guild.icon.url if member.guild.icon else None
        )
        await channel.send(embed=e)
    except Exception:
        pass

@bot.event
async def on_member_remove(member):
    try:
        channel = member.guild.system_channel
        if not channel:
            return
        e = make_embed(
            "Goodbye!",
            f"**{member.name}** has left the server.",
            DANGER
        )
        e.set_thumbnail(url=member.display_avatar.url)
        e.set_footer(text=f"Members: {member.guild.member_count}")
        await channel.send(embed=e)
    except Exception:
        pass

# --- MODERATION ---
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason"):
    if member == ctx.author:
        return await ctx.send(embed=make_embed("Error", "You can't ban yourself.", DANGER), delete_after=5)
    if member.top_role >= ctx.author.top_role:
        return await ctx.send(embed=make_embed("Error", "You can't ban someone with equal/higher role.", DANGER), delete_after=5)
    e = make_embed("BANNED", f"{member.mention} has been banned.", DANGER)
    e.add_field(name="Reason", value=reason, inline=False)
    e.set_thumbnail(url=member.display_avatar.url)
    e.set_footer(text=f"Banned by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=e)
    await member.ban(reason=reason)

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member_name):
    banned = [entry async for entry in ctx.guild.bans()]
    for ban_entry in banned:
        if ban_entry.user.name.lower() == member_name.lower():
            await ctx.guild.unban(ban_entry.user)
            e = make_embed("UNBANNED", f"**{ban_entry.user}** has been unbanned.", SUCCESS)
            e.set_footer(text=f"Unbanned by {ctx.author}", icon_url=ctx.author.display_avatar.url)
            await ctx.send(embed=e)
            return
    await ctx.send(embed=make_embed("Not Found", "No banned user with that name.", DANGER), delete_after=5)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason"):
    if member == ctx.author:
        return await ctx.send(embed=make_embed("Error", "You can't kick yourself.", DANGER), delete_after=5)
    e = make_embed("KICKED", f"{member.mention} has been kicked.", WARNING)
    e.add_field(name="Reason", value=reason, inline=False)
    e.set_thumbnail(url=member.display_avatar.url)
    e.set_footer(text=f"Kicked by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=e)
    await member.kick(reason=reason)

@bot.command()
@commands.has_permissions(moderate_members=True)
async def mute(ctx, member: discord.Member, minutes: int = 10):
    await member.timeout(discord.utils.utcnow() + discord.timedelta(minutes=minutes))
    e = make_embed("MUTED", f"{member.mention} has been muted for **{minutes} minutes**.", WARNING)
    e.set_thumbnail(url=member.display_avatar.url)
    e.set_footer(text=f"Muted by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=e)

@bot.command()
@commands.has_permissions(moderate_members=True)
async def unmute(ctx, member: discord.Member):
    await member.timeout(None)
    e = make_embed("UNMUTED", f"{member.mention} has been unmuted.", SUCCESS)
    e.set_thumbnail(url=member.display_avatar.url)
    await ctx.send(embed=e)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member: discord.Member, *, reason="No reason"):
    e = make_embed("WARNING", f"{member.mention} has been warned.", WARNING)
    e.add_field(name="Reason", value=reason, inline=False)
    e.set_thumbnail(url=member.display_avatar.url)
    e.set_footer(text=f"Warned by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=e)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def slowmode(ctx, seconds: int = 0):
    await ctx.channel.edit(slowmode_delay=seconds)
    e = make_embed("SLOWMODE", f"Slowmode set to **{seconds} seconds**.", SUCCESS)
    await ctx.send(embed=e)

# --- FUN ---
@bot.command(name="8ball")
async def eight_ball(ctx, *, question):
    responses = [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes, definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.",
        "Better not tell you now.", "Cannot predict now.",
        "Concentrate and ask again.", "Don't count on it.",
        "My reply is no.", "My sources say no.",
        "Outlook not so good.", "Very doubtful."
    ]
    e = make_embed("8BALL", color=PURPLE)
    e.add_field(name="Question", value=question, inline=False)
    e.add_field(name="Answer", value=f"*{random.choice(responses)}*", inline=False)
    e.set_footer(text=f"Asked by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=e)

@bot.command()
async def coinflip(ctx):
    result = random.choice(["Heads", "Tails"])
    emoji = "🪙" if result == "Heads" else "🔴"
    e = make_embed("COINFLIP", f"{emoji} **{result}!**", PURPLE)
    await ctx.send(embed=e)

@bot.command()
async def dice(ctx):
    dice_faces = {
        1: "⚀", 2: "⚁", 3: "⚂",
        4: "⚃", 5: "⚄", 6: "⚅"
    }
    result = random.randint(1, 6)
    e = make_embed("DICE", f"{dice_faces[result]} You rolled a **{result}**", PURPLE)
    await ctx.send(embed=e)

@bot.command()
async def poll(ctx, *, question):
    e = make_embed("POLL", f"**{question}**", PURPLE)
    e.set_footer(text=f"Poll by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    msg = await ctx.send(embed=e)
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")

@bot.command()
async def say(ctx, *, message):
    e = make_embed(description=message, color=PURPLE)
    e.set_footer(text=f"Sent by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=e)

# --- UTILITY ---
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    roles = [role.mention for role in member.roles[1:]]
    flags = [f.replace("_", " ").title() for f in member.public_flags.all()]
    e = make_embed(member.display_name, color=SUCCESS)
    e.set_thumbnail(url=member.display_avatar.url)
    e.add_field(name="Joined Server", value=f"<t:{int(member.joined_at.timestamp())}:R>", inline=True)
    e.add_field(name="Account Created", value=f"<t:{int(member.created_at.timestamp())}:R>", inline=True)
    e.add_field(name="ID", value=f"`{member.id}`", inline=True)
    if roles:
        e.add_field(name=f"Roles [{len(roles)}]", value=" ".join(roles[:20]) + ("..." if len(roles) > 20 else ""), inline=False)
    e.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=e)

@bot.command()
async def membercount(ctx):
    e = make_embed(ctx.guild.name, color=SUCCESS)
    e.add_field(name="Total", value=f"`{ctx.guild.member_count}`", inline=True)
    e.add_field(name="Humans", value=f"`{sum(1 for m in ctx.guild.members if not m.bot)}`", inline=True)
    e.add_field(name="Bots", value=f"`{sum(1 for m in ctx.guild.members if m.bot)}`", inline=True)
    if ctx.guild.icon:
        e.set_thumbnail(url=ctx.guild.icon.url)
    await ctx.send(embed=e)

@bot.command()
async def serverinfo(ctx):
    g = ctx.guild
    e = make_embed(g.name, color=SUCCESS)
    if g.icon:
        e.set_thumbnail(url=g.icon.url)
    if g.banner:
        e.set_image(url=g.banner.url)
    e.add_field(name="Owner", value=g.owner.mention, inline=True)
    e.add_field(name="Members", value=f"`{g.member_count}`", inline=True)
    e.add_field(name="Channels", value=f"`{len(g.channels)}`", inline=True)
    e.add_field(name="Roles", value=f"`{len(g.roles)}`", inline=True)
    e.add_field(name="Emojis", value=f"`{len(g.emojis)}`", inline=True)
    e.add_field(name="Boosts", value=f"`{g.premium_subscription_count}`", inline=True)
    e.add_field(name="Created", value=f"<t:{int(g.created_at.timestamp())}:R>", inline=True)
    e.add_field(name="Verification", value=str(g.verification_level).title(), inline=True)
    e.set_footer(text=f"ID: {g.id}")
    await ctx.send(embed=e)

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    e = make_embed(f"{member.display_name}'s Avatar", color=SUCCESS)
    e.set_image(url=member.display_avatar.with_size(1024).url)
    e.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=e)

@bot.command()
async def remind(ctx, minutes: int, *, message):
    e = make_embed("Reminder Set", f"I'll remind you in **{minutes} minute(s)**\n> {message}", SUCCESS)
    e.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=e)
    await asyncio.sleep(minutes * 60)
    try:
        dm_embed = make_embed("Reminder", f"**{message}**", BLURPLE)
        await ctx.author.send(embed=dm_embed)
    except discord.Forbidden:
        pass

@bot.command()
async def calc(ctx, *, expression):
    allowed = set("0123456789+-*/.() %")
    if not all(c in allowed for c in expression):
        return await ctx.send(embed=make_embed("Error", "Only math characters allowed.", DANGER), delete_after=5)
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        e = make_embed("Calculator", color=SUCCESS)
        e.add_field(name="Expression", value=f"`{expression}`", inline=False)
        e.add_field(name="Result", value=f"**{result}**", inline=False)
        await ctx.send(embed=e)
    except Exception:
        await ctx.send(embed=make_embed("Error", "Invalid math expression.", DANGER), delete_after=5)

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    if latency < 100:
        bar = "🟩🟩🟩🟩🟩"
        status = "Excellent"
    elif latency < 200:
        bar = "🟨🟨🟨🟩🟩"
        status = "Good"
    elif latency < 350:
        bar = "🟧🟧🟩🟩🟩"
        status = "Okay"
    else:
        bar = "🟥🟩🟩🟩🟩"
        status = "Poor"
    e = make_embed("PONG!", f"Latency: **{latency}ms** {bar}\nStatus: **{status}**", SUCCESS)
    await ctx.send(embed=e)

@bot.command()
async def uptime(ctx):
    if not bot.launch_time:
        return await ctx.send(embed=make_embed("Error", "Launch time not recorded.", DANGER), delete_after=5)
    seconds = int(time.time() - bot.launch_time)
    hours, remainder = divmod(seconds, 3600)
    mins, secs = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    e = make_embed("UPTIME", f"**{days}d {hours}h {mins}m {secs}s**", SUCCESS)
    await ctx.send(embed=e)

@bot.command()
async def hello(ctx):
    greetings = ["Hey there!", "Hello!", "Hi!", "Yo!", "What's up!", "Howdy!"]
    e = make_embed(description=f"{random.choice(greetings)} {ctx.author.mention}!", color=SUCCESS)
    e.set_thumbnail(url=ctx.bot.user.display_avatar.url)
    await ctx.send(embed=e)

# --- ADMIN ---
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    deleted = await ctx.channel.purge(limit=amount + 1)
    e = make_embed("CLEARED", f"Deleted **{len(deleted) - 1}** messages.", SUCCESS)
    await ctx.send(embed=e, delete_after=3)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    e = make_embed("CHANNEL LOCKED", "This channel has been locked.", DANGER)
    await ctx.send(embed=e)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    e = make_embed("CHANNEL UNLOCKED", "This channel has been unlocked.", SUCCESS)
    await ctx.send(embed=e)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def announce(ctx, *, message):
    e = make_embed("ANNOUNCEMENT", message, WARNING)
    e.set_footer(text=f"Announced by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=e)

# --- ROLES ---
@bot.command()
@commands.has_permissions(manage_roles=True)
async def giverole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    e = make_embed("ROLE GIVEN", f"Added {role.mention} to {member.mention}", SUCCESS)
    await ctx.send(embed=e)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    e = make_embed("ROLE REMOVED", f"Removed {role.mention} from {member.mention}", WARNING)
    await ctx.send(embed=e)

# --- GIVEAWAY ---
@bot.command()
@commands.has_permissions(manage_messages=True)
async def giveaway(ctx, time: int, *, prize):
    e = make_embed(
        "GIVEAWAY!",
        f"Prize: **{prize}**\nReact with 🎉 to enter!\nEnds in **{time} second(s)**",
        WARNING
    )
    e.set_footer(text=f"Started by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    msg = await ctx.send(embed=e)
    await msg.add_reaction("🎉")
    await asyncio.sleep(time)
    new_msg = await ctx.channel.fetch_message(msg.id)
    users = [user async for user in new_msg.reactions[0].users() if not user.bot]
    if users:
        winner = random.choice(users)
        e = make_embed("GIVEAWAY ENDED", f"🎉 {winner.mention} won **{prize}**!", WARNING)
        e.set_thumbnail(url=winner.display_avatar.url)
        await ctx.send(embed=e)
    else:
        e = make_embed("GIVEAWAY ENDED", "No one entered the giveaway.", DANGER)
        await ctx.send(embed=e)

bot.run(token)
