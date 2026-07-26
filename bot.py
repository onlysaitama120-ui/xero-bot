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

@bot.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(
        title="Xero Bot Commands",
        description="Use `!help <command>` for more info on a command",
        color=discord.Color.blurple()
    )
    embed.set_thumbnail(url=ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url)
    embed.add_field(name="Moderation", value="`ban` `kick` `unban` `mute` `unmute` `warn` `slowmode` `clear` `lock` `unlock`", inline=False)
    embed.add_field(name="Fun", value="`8ball` `coinflip` `dice` `poll` `say`", inline=False)
    embed.add_field(name="Utility", value="`userinfo` `serverinfo` `membercount` `avatar` `remind` `calc`", inline=False)
    embed.add_field(name="Roles", value="`giverole` `removerole`", inline=False)
    embed.add_field(name="Admin", value="`announce` `giveaway`", inline=False)
    embed.set_footer(text="Xero Bot", icon_url=ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url)
    await ctx.send(embed=embed)

@help.command(name="ban")
async def help_ban(ctx):
    embed = discord.Embed(title="!ban", description="Ban a member from the server", color=discord.Color.red())
    embed.add_field(name="Usage", value="`!ban @user reason`", inline=False)
    embed.add_field(name="Permission", value="Ban Members", inline=False)
    await ctx.send(embed=embed)

@help.command(name="kick")
async def help_kick(ctx):
    embed = discord.Embed(title="!kick", description="Kick a member from the server", color=discord.Color.red())
    embed.add_field(name="Usage", value="`!kick @user reason`", inline=False)
    embed.add_field(name="Permission", value="Kick Members", inline=False)
    await ctx.send(embed=embed)

@help.command(name="unban")
async def help_unban(ctx):
    embed = discord.Embed(title="!unban", description="Unban a user by username", color=discord.Color.red())
    embed.add_field(name="Usage", value="`!unban username`", inline=False)
    embed.add_field(name="Permission", value="Ban Members", inline=False)
    await ctx.send(embed=embed)

@help.command(name="mute")
async def help_mute(ctx):
    embed = discord.Embed(title="!mute", description="Timeout a member", color=discord.Color.orange())
    embed.add_field(name="Usage", value="`!mute @user minutes`", inline=False)
    embed.add_field(name="Permission", value="Moderate Members", inline=False)
    await ctx.send(embed=embed)

@help.command(name="unmute")
async def help_unmute(ctx):
    embed = discord.Embed(title="!unmute", description="Remove timeout from a member", color=discord.Color.orange())
    embed.add_field(name="Usage", value="`!unmute @user`", inline=False)
    embed.add_field(name="Permission", value="Moderate Members", inline=False)
    await ctx.send(embed=embed)

@help.command(name="warn")
async def help_warn(ctx):
    embed = discord.Embed(title="!warn", description="Warn a member", color=discord.Color.orange())
    embed.add_field(name="Usage", value="`!warn @user reason`", inline=False)
    embed.add_field(name="Permission", value="Manage Messages", inline=False)
    await ctx.send(embed=embed)

@help.command(name="clear")
async def help_clear(ctx):
    embed = discord.Embed(title="!clear", description="Bulk delete messages", color=discord.Color.orange())
    embed.add_field(name="Usage", value="`!clear amount`", inline=False)
    embed.add_field(name="Permission", value="Manage Messages", inline=False)
    await ctx.send(embed=embed)

@help.command(name="lock")
async def help_lock(ctx):
    embed = discord.Embed(title="!lock", description="Lock the current channel", color=discord.Color.orange())
    embed.add_field(name="Usage", value="`!lock`", inline=False)
    embed.add_field(name="Permission", value="Manage Channels", inline=False)
    await ctx.send(embed=embed)

@help.command(name="unlock")
async def help_unlock(ctx):
    embed = discord.Embed(title="!unlock", description="Unlock the current channel", color=discord.Color.orange())
    embed.add_field(name="Usage", value="`!unlock`", inline=False)
    embed.add_field(name="Permission", value="Manage Channels", inline=False)
    await ctx.send(embed=embed)

@help.command(name="8ball")
async def help_8ball(ctx):
    embed = discord.Embed(title="!8ball", description="Ask the magic 8ball a question", color=discord.Color.purple())
    embed.add_field(name="Usage", value="`!8ball question`", inline=False)
    await ctx.send(embed=embed)

@help.command(name="coinflip")
async def help_coinflip(ctx):
    embed = discord.Embed(title="!coinflip", description="Flip a coin", color=discord.Color.purple())
    embed.add_field(name="Usage", value="`!coinflip`", inline=False)
    await ctx.send(embed=embed)

@help.command(name="dice")
async def help_dice(ctx):
    embed = discord.Embed(title="!dice", description="Roll a dice", color=discord.Color.purple())
    embed.add_field(name="Usage", value="`!dice`", inline=False)
    await ctx.send(embed=embed)

@help.command(name="poll")
async def help_poll(ctx):
    embed = discord.Embed(title="!poll", description="Create a yes/no poll", color=discord.Color.purple())
    embed.add_field(name="Usage", value="`!poll question`", inline=False)
    await ctx.send(embed=embed)

@help.command(name="say")
async def help_say(ctx):
    embed = discord.Embed(title="!say", description="Make the bot say something", color=discord.Color.purple())
    embed.add_field(name="Usage", value="`!say message`", inline=False)
    await ctx.send(embed=embed)

@help.command(name="userinfo")
async def help_userinfo(ctx):
    embed = discord.Embed(title="!userinfo", description="Get info about a member", color=discord.Color.blue())
    embed.add_field(name="Usage", value="`!userinfo @user`", inline=False)
    await ctx.send(embed=embed)

@help.command(name="serverinfo")
async def help_serverinfo(ctx):
    embed = discord.Embed(title="!serverinfo", description="Get info about the server", color=discord.Color.blue())
    embed.add_field(name="Usage", value="`!serverinfo`", inline=False)
    await ctx.send(embed=embed)

@help.command(name="avatar")
async def help_avatar(ctx):
    embed = discord.Embed(title="!avatar", description="Get a member's avatar", color=discord.Color.blue())
    embed.add_field(name="Usage", value="`!avatar @user`", inline=False)
    await ctx.send(embed=embed)

@help.command(name="remind")
async def help_remind(ctx):
    embed = discord.Embed(title="!remind", description="Set a reminder", color=discord.Color.blue())
    embed.add_field(name="Usage", value="`!remind minutes message`", inline=False)
    await ctx.send(embed=embed)

@help.command(name="calc")
async def help_calc(ctx):
    embed = discord.Embed(title="!calc", description="Calculate math", color=discord.Color.blue())
    embed.add_field(name="Usage", value="`!calc 2+2`", inline=False)
    await ctx.send(embed=embed)

@help.command(name="giverole")
async def help_giverole(ctx):
    embed = discord.Embed(title="!giverole", description="Give a role to a member", color=discord.Color.green())
    embed.add_field(name="Usage", value="`!giverole @user @role`", inline=False)
    embed.add_field(name="Permission", value="Manage Roles", inline=False)
    await ctx.send(embed=embed)

@help.command(name="removerole")
async def help_removerole(ctx):
    embed = discord.Embed(title="!removerole", description="Remove a role from a member", color=discord.Color.green())
    embed.add_field(name="Usage", value="`!removerole @user @role`", inline=False)
    embed.add_field(name="Permission", value="Manage Roles", inline=False)
    await ctx.send(embed=embed)

@help.command(name="announce")
async def help_announce(ctx):
    embed = discord.Embed(title="!announce", description="Send an announcement embed", color=discord.Color.gold())
    embed.add_field(name="Usage", value="`!announce message`", inline=False)
    embed.add_field(name="Permission", value="Manage Messages", inline=False)
    await ctx.send(embed=embed)

@help.command(name="giveaway")
async def help_giveaway(ctx):
    embed = discord.Embed(title="!giveaway", description="Start a giveaway", color=discord.Color.gold())
    embed.add_field(name="Usage", value="`!giveaway seconds prize`", inline=False)
    embed.add_field(name="Example", value="`!giveaway 60 Nitro`", inline=False)
    embed.add_field(name="Permission", value="Manage Messages", inline=False)
    await ctx.send(embed=embed)

# --- WELCOME MESSAGE ---
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    embed = discord.Embed(
        title=f"Welcome {member.name}!",
        description=f"Enjoy your stay in {member.guild.name}!",
        color=discord.Color.green()
    )
    embed.set_image(url="https://your-image-url.com/pic.png")
    await channel.send(embed=embed)

# --- MODERATION ---
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason"):
    await member.ban(reason=reason)
    await ctx.send(f"{member} has been banned. Reason: {reason}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member_name):
    banned = [entry async for entry in ctx.guild.bans()]
    for ban_entry in banned:
        if ban_entry.user.name == member_name:
            await ctx.guild.unban(ban_entry.user)
            await ctx.send(f"{ban_entry.user} has been unbanned")
            return

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason"):
    await member.kick(reason=reason)
    await ctx.send(f"{member} has been kicked. Reason: {reason}")

@bot.command()
@commands.has_permissions(moderate_members=True)
async def mute(ctx, member: discord.Member, minutes: int = 10):
    await member.timeout(discord.utils.utcnow() + discord.timedelta(minutes=minutes))
    await ctx.send(f"{member} has been muted for {minutes} minutes")

@bot.command()
@commands.has_permissions(moderate_members=True)
async def unmute(ctx, member: discord.Member):
    await member.timeout(None)
    await ctx.send(f"{member} has been unmuted")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member: discord.Member, *, reason="No reason"):
    embed = discord.Embed(title="Warning", description=f"{member.mention} has been warned\nReason: {reason}", color=discord.Color.red())
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def slowmode(ctx, seconds: int = 0):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Slowmode set to {seconds} seconds")

# --- FUN ---
@bot.command(name="8ball")
async def eight_ball(ctx, *, question):
    responses = ["Yes", "No", "Maybe", "Ask again later", "Definitely", "Absolutely not", "Most likely", "Doubtful"]
    await ctx.send(f"🎱 {random.choice(responses)}")

@bot.command()
async def coinflip(ctx):
    result = random.choice(["Heads", "Tails"])
    await ctx.send(f"🪙 {result}!")

@bot.command()
async def dice(ctx):
    result = random.randint(1, 6)
    await ctx.send(f"🎲 You rolled a **{result}**")

@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="Poll", description=question, color=discord.Color.blue())
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")

@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

# --- UTILITY ---
@bot.command()
async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(title=member.display_name, color=discord.Color.blue())
    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
    embed.add_field(name="Joined", value=member.joined_at.strftime("%d/%m/%Y"))
    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Roles", value=len(member.roles))
    await ctx.send(embed=embed)

@bot.command()
async def membercount(ctx):
    await ctx.send(f"Total members: {ctx.guild.member_count}")

@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    embed = discord.Embed(title=guild.name, color=discord.Color.green())
    embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
    embed.add_field(name="Members", value=guild.member_count)
    embed.add_field(name="Channels", value=len(guild.channels))
    embed.add_field(name="Roles", value=len(guild.roles))
    embed.add_field(name="Created", value=guild.created_at.strftime("%d/%m/%Y"))
    await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"{member.display_name}'s Avatar", color=discord.Color.blue())
    embed.set_image(url=member.avatar.url if member.avatar else member.default_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def remind(ctx, minutes: int, *, message):
    await ctx.send(f"⏰ I'll remind you in {minutes} minutes: {message}")
    await asyncio.sleep(minutes * 60)
    await ctx.author.send(f"⏰ Reminder: {message}")

@bot.command()
async def calc(ctx, *, expression):
    try:
        result = eval(expression)
        await ctx.send(f"🧮 {expression} = **{result}**")
    except:
        await ctx.send("Invalid math expression")

# --- ADMIN ---
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    deleted = await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"Deleted {len(deleted) - 1} messages", delete_after=3)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send("🔒 Channel locked")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send("🔓 Channel unlocked")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def announce(ctx, *, message):
    embed = discord.Embed(title="Announcement", description=message, color=discord.Color.gold())
    await ctx.send(embed=embed)

# --- ROLES ---
@bot.command()
@commands.has_permissions(manage_roles=True)
async def giverole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"Added {role.name} to {member.display_name}")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    await ctx.send(f"Removed {role.name} from {member.display_name}")

# --- GIVEAWAY ---
@bot.command()
@commands.has_permissions(manage_messages=True)
async def giveaway(ctx, time: int, *, prize):
    embed = discord.Embed(
        title="GIVEAWAY!",
        description=f"Prize: **{prize}**\nReact with 🎉 to enter!\nEnds in {time} seconds",
        color=discord.Color.gold()
    )
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("🎉")
    await asyncio.sleep(time)
    new_msg = await ctx.channel.fetch_message(msg.id)
    users = [user async for user in new_msg.reactions[0].users() if not user.bot]
    if users:
        winner = random.choice(users)
        await ctx.send(f"🎉 Congratulations {winner.mention}! You won **{prize}**!")
    else:
        await ctx.send("No one entered the giveaway.")

# --- MISC ---
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.display_name}!")

bot.run(token)