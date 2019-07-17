import discord
import talk

with open("key.txt" ,"r") as file:
    TOKEN=file.read().replace('\n','')
print(str(TOKEN))
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ring'):
        words =message.content[6:]
        print(words)
        talk.play(words)
        await message.channel.send(str('Paging the Garrage! | '+words))


client.run(str(TOKEN))
