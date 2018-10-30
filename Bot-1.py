import discord
from discord.ext import commands

TOKEN = 'NTA2ODIzNzQyODc4Mzg0MTQ4.DrnwJw.lPqpVJWqk0iqz0XfscA9_p8WZW0'

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot Ready.')

#Basic Commands

@client.event
async def on_message(message):
    channel = message.channel
    author = message.author
    content = message.content
    print('{} - {}'.format(author, content))
    if message.content.startswith('!ping'):
        await client.send_message(channel, 'Pong!')
    if message.content.startswith('!support'):
        await client.send_message(channel, 'http://nolanhepworth.me/')

client.run(TOKEN)
