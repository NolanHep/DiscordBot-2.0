import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import youtube_dl

TOKEN = 'NTA2ODIzNzQyODc4Mzg0MTQ4.DrnwJw.lPqpVJWqk0iqz0XfscA9_p8WZW0'

client = commands.Bot(command_prefix='!')
status = ['nolanhepworth.me', 'Type !Help', 'Type !Support']
players = {}
queues = {}

def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()
async def status_change():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(5)

@client.event
async def on_ready():
    print('Bot Online.')

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@client.command(pass_context=True)
async def queue(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))

    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    await client.say('Queued.')


@client.command()
async def Help():
    embed = discord.Embed(
        title = '',
        description = 'An Overview of this bots commands.',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='Written by Nolan!.')
    embed.set_image(url='https://i.imgur.com/T1L8arS.png')
    embed.set_thumbnail(url='https://www.ledr.com/colours/blue.jpg')
    embed.set_author(name='Help')
    icon_url='https://i.imgur.com/T1L8arS.png'
    embed.add_field(name='!play', value='Plays video audio. !play youtubeurl, !queue youtubeurl', inline=True)
    embed.add_field(name='!Reddit', value='Displays whole reddit post!', inline=True)
    embed.add_field(name='!Challenge', value='Coming Soon', inline=True)
    embed.add_field(name='!Stats', value='Coming Soon', inline=False)

    await client.say(embed=embed)

client.loop.create_task(status_change())
client.run(TOKEN)
