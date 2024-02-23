import discord
import os
from discord.ext import tasks

token = os.environ['DISCORD_BOT_TOKEN']
channel = os.environ['DISCORD_CHANNEL_ID']
message = os.environ['DISCORD_MESSAGE_UP']

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("Scanning servers"))
    print('Bot is ready')
    is_up.start()

@tasks.loop(minutes=10)
async def is_up():
    message_channel = client.get_channel(int(channel))
    print(f"Got channel {message_channel}")
    await message_channel.send(message)

@is_up.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")

client.run(token)