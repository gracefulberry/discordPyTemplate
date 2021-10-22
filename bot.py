# import startements
import os
from dotenv import load_dotenv

from discord.ext import commands

# authenticate token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='temp')
async def temp_com(ctx):

    await ctx.send(f"I am {bot.user.name}")


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

bot.run(TOKEN)
