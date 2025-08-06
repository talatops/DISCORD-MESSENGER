import discord
from discord.ext import commands
import os, traceback
from assets import functions as func
from config import Token

# Set up intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True

bot = commands.Bot(case_insensitive=True, command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print('*********\nBot is Ready.\n*********')

async def CheckAdmin(ctx):
    # Check if we're in a guild (server) context
    if ctx.guild is None:
        await ctx.send(embed=func.ErrorEmbed('Server Only', 'This bot only works in servers, not in DMs.'))
        return False
    
    # Check if author is a Member object with guild permissions
    if hasattr(ctx.author, 'guild_permissions') and ctx.author.guild_permissions.administrator:
        return True
    else:
        await ctx.send(embed=func.ErrorEmbed('Missing Permissions', 'You are missing permissions. You need to have `administrator` permission in order to use this bot.'))
        return False

bot.remove_command('help')
bot.check_once(CheckAdmin)

@bot.command()
async def ping(ctx):
    await ctx.send (f"📶 {round(bot.latency * 1000)}ms")

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, (commands.CommandNotFound, commands.CheckFailure)):
        return

for file in os.listdir('./cogs'):
    if file.endswith('.py') and file != '__init__.py':
        try:
            bot.load_extension("cogs."+file[:-3])
            print(f"{file[:-3]} Loaded successfully.")
        except:
            print(f"Unable to load {file[:-3]}.")
            print(traceback.format_exc())

bot.run(Token)
