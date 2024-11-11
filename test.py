import discord
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = "MTMwNDcxMDgzMjYyOTg3NDc0OQ.Gr2N8d.rQIcqgYYjx_ZfQbewRu3D1gD4rDI0n7Lb35UuE"

random_contents=[
    "なにもかんがえたくない",
    "かんがえてみようかな",
    "考えよう",
]

@client.event
async def on_ready():
    print("login done")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/yo'):
        await message.channel.send('yo!')

client.run(TOKEN)