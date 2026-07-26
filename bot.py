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

bot = commands.Bot(command_prefix="!", intents=intents)

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