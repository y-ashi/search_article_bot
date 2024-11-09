import discord

# インテントの生成
intents = discord.Intents.default()
intents.message_content = True

# クライアントの生成
client = discord.Client(intents=intents)

# discordと接続した時に呼ばれる
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# メッセージを受信した時に呼ばれる
@client.event
async def on_message(message):
    # 自分のメッセージを無効
    if message.author == client.user:
        return

    # メッセージが"$hello"で始まっていたら"Hello!"と応答
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# クライアントの実行
client.run('MTMwNDcxMDgzMjYyOTg3NDc0OQ.Gr2N8d.rQIcqgYYjx_ZfQbewRu3D1gD4rDI0n7Lb35UuE')