import discord
from discord.ext import commands

TOKEN = ''

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot Ready.')

client.run(TOKEN)

