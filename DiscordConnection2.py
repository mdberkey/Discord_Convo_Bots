import asyncio
import random

import discord
from discord.ext import commands

from GetRandomEmoji import getRandomEmoji
from GoogleSearch import googleSearch
from MarkovGeneration import generation
from TextToSpeech import TTSus

# Clockster the bot
TOKEN = 'NzE2MTIxMTU4MzQ4NDM5NjM0.XtHJzQ.2W2i3005OHtJ2xWzn887_fN_JIQ'

client = commands.Bot(command_prefix='$')
channel = client.get_channel(339964184223809547)            # text channel


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='with the fabric of spacetime'))
    print('client ready')


@client.command(pass_context=True)
async def start(ctx):
    vChannel = client.get_channel(339964184223809548)       # voice channel
    await vChannel.connect()


@client.command(pass_context=True)
async def end(ctx):
    vGuild = ctx.guild
    voice_client = vGuild.voice_client
    await voice_client.disconnect()


@client.event
async def on_message(message):

    if message.author == client.user:                                           # ignores its own messages
        return
    elif message.content.startswith('$' or 'http'):                           # ignores commands and links
        await client.process_commands(message)
        return
    elif message.author.id == 713862841668730920:                               # user that bot responds to
        response = generation.main(message.content)
        channel = client.get_channel(716458739074465813)

        # random numbers for reactions and link probabilities
        randNumA = random.randint(1, 10)
        randNumB = random.randint(1, 10)

        # converts text response to voice that is played in the voice channel
        TTSus(response)
        vGuild = message.guild
        voice_client = vGuild.voice_client
        voice_client.play(discord.FFmpegPCMAudio('audio.mp3'), after=None)

        # adds typing appearance
        while voice_client.is_playing():
            async with channel.typing():
                await asyncio.sleep(1)
        await channel.send(response)

        # sends a related link about 20% of the time
        if randNumA > 7:
            link = googleSearch(response)
            if link:
                await channel.send(link)

        # reacts to the previous message with emoticons 40%
        if randNumB > 6:
            for i in range(random.randint(1, 5)):
                await message.add_reaction(getRandomEmoji())

    # allows other commands to be used
    await client.process_commands(message)

client.run(TOKEN)
