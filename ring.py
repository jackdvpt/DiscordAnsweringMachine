import discord

with open("key.txt" ,"r") as file:
    TOKEN=file.read()/replace('\n','')
print(str(TOKEN))
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


client.run(str(TOKEN))
