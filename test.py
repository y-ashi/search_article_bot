import discord
import random

TOKEN='MTMwNDcxMDgzMjYyOTg3NDc0OQ.Gr2N8d.rQIcqgYYjx_ZfQbewRu3D1gD4rDI0n7Lb35UuE'

intents = discord.Intents.default()

client = discord.Client(intents=intents)

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
    if message.content == "/yo":
        content = random.choice(random_contents)
        await message.channel.send(content)
client.run(TOKEN)