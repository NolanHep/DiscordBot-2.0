import discord
from discord.ext import commands

TOKEN = 'NTA2ODIzNzQyODc4Mzg0MTQ4.DrnwJw.lPqpVJWqk0iqz0XfscA9_p8WZW0'

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot Ready.')

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))

client.run(TOKEN)

