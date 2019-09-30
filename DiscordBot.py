import config
import discord
from discord.ext import commands
import asyncio
from itertools import cycle
from datetime import datetime

now = datetime.now
client = commands.Bot(command_prefix = '$')
status = ['V0.55','WIP']

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed():
        current_status = next(msgs)
        await client.change_presence(activity=discord.Game(name=current_status))
        await asyncio.sleep(30)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$time'):
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)	

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$ping'):
        await message.channel.send('pong!')

    if message.content.startswith('$creator'):
        await message.channel.send('Ana is my creator. I am designed as a test model and to help them learn Python along with other languages. I will be devolped in their freetime and when they are learning in University.')

client.loop.create_task(change_status())

client.run(config.TOKEN)
