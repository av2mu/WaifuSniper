import discord

import bot_token

client = discord.Client()

@client.event
async def on_ready():
    print('ready to go!')

@client.event
async def on_message(message):
    print(message.author.id)

    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.add_reaction('👍')
    if message.author.id == 432610292342587392:
        await message.add_reaction('👍')





client.run(bot_token.bot_token)