import discord

TOKEN = 'NjAwOTY4MTEzMDU1NTk2NTU1.XS7dWw.bJg320N2VXGS9G50X7hYWar8r4g'


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        print(message.content)
        await message.channel.send('Hello!')


client.run(TOKEN)
