import discord
import talk
import scramble

with open("key.txt" ,"r") as file:
    TOKEN=file.read().replace('\n','')
print(str(TOKEN))
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(600968470003449858)
    await channel.send("IM ALIVE")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ring'):
        words =message.content[6:]
        print(words)
        talk.play(words, message.author.display_name)
        await message.channel.send(str('Paging the Garrage! | '+words))

    if message.content.startswith('$scramble'):
        words =message.content[6:]
        scramble.roundtranslate(words, message.author.display_name)
        await message.channel.send(str('Paging the Garrage! | '+words))

    if message.content.startswith("%rick"):
        talk.play("Hey Google play never gonna give you up",message.author.display_name)
        await message.channel.send("That felt strange")

client.run(str(TOKEN))
