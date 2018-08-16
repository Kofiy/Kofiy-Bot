import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Game
import asyncio
import json
import os.path
import random
import requests


BOT_PREFIX = "k!"
client = Bot(command_prefix=BOT_PREFIX)

BOT_TOKEN = "THIS_IS_MY_BOT_TOKEN"

 #This is for me
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='k!help'))
    print(client.user.name)
    print("-------------------")
    print("""
Hello! I'm ready 
    """)
#commands
@client.command(pass_context=True)
async def say(ctx, * , message):
    await client.say(message)

@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])
    

@client.event
async def on_message(message):

    if message.content.startswith('k!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('k!ping'):
        msg = '**{0.author.mention} Pong!**'.format(message)
        await client.send_message(message.channel, msg)
        
    if message.content == 'k!embed':
        embed = discord.Embed(title="Title", description="This is a __test__ `embed`", color=0x00ff00)
        await client.send_message(message.channel, embed=embed)
        
        
    if message.content == 'k!game':
        member = message.author
        game = discord.Game
        if member.game == None:
            await client.send_message(message.channel, "You aren't playing")
        else:
            await client.send_message(message.channel, "You are playing {}" .format(member.game))

    if message.content.lower().startswith('k!love'):
        await client.send_message(message.channel, ''' 
───▄▄▄▄▄▄─────▄▄▄▄▄▄
─▄█▓▓▓▓▓▓█▄─▄█▓▓▓▓▓▓█▄
▐█▓▓▒▒▒▒▒▓▓█▓▓▒▒▒▒▒▓▓█▌
█▓▓▒▒░╔╗╔═╦═╦═╦═╗░▒▒▓▓█
█▓▓▒▒░║╠╣╬╠╗║╔╣╩╣░▒▒▓▓█
▐█▓▓▒▒╚═╩═╝╚═╝╚═╝▒▒▓▓█▌
─▀█▓▓▒▒░░░░░░░░░▒▒▓▓█▀
───▀█▓▓▒▒░░░░░▒▒▓▓█▀
─────▀█▓▓▒▒░▒▒▓▓█▀
──────▀█▓▓▒▓▓█▀
────────▀█▓█▀
──────────▀
        ''',)
        await client.send_message(message.channel, "I love you!")

    if message.content.lower().startswith('k!transparent'):
        photo = discord.Embed(color=0xFAFAFA)
        photo.set_image(url="https://cdn.discordapp.com/attachments/436883644473409538/466926711448272899/trump.png")
        await client.send_message(message.channel, embed=photo)

    if message.content == 'k!game_over':
        over = discord.Embed(color=0xFAFAFA)
        over.set_image(url="https://cdn.discordapp.com/attachments/465256769690796033/465941825597997066/triggered.gif")
        botmag = await client.send_message(message.channel, embed=over)
    
        await client.add_reaction(botmag, '🆗')

    if message.content.lower().startswith('k!lol'):
        await client.send_message(message.channel, ":rofl: LOL :rofl: !")
        
   #if message.content.lower().startswith('k!server-invite'):
       #SInvite = await client.create_invite(message.channel, max_age="99999"
       #await client.send_message(message.channel,'{}' .format(SInvite))

    if message.content.lower().startswith('k!invite'):
        invite = discord.Embed(title="https://discordapp.com/oauth2/authorize?client_id=457633173669412875&scope=bot&permissions=2146958847", color=random.randint(0, 0xFFFFFF))
        invite.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXW5NdMhsu1G6xmAMbnyP7jcEDery1bi7Yk84CHBj9ilcXlTsQrw")
        await client.send_message(message.channel, embed=invite)

    if message.content.lower().startswith('k!party'):
        party = discord.Embed(color=0x12AD4F)
        party.set_image(url="https://giphy.com/gifs/carnaval-carnival-dance-10hO3rDNqqg2Xe")
        await client.send_message(message.channel, embed=party)
        
    if message.content.lower().startswith('k!messages'):
        counter = 0
        wait = discord.Embed(title="Calculating messages...")
        tmp = await client.send_message(message.channel, embed=wait)
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        counmes = discord.Embed(title="You have {} messages.".format(counter), color=random.randint(0, 0xFFFFFF))
        await client.edit_message(tmp, embed=counmes)


    if message.content.lower().startswith('k!xp'):
        await client.send_message(message.channel, """```css
You have {} XP!```
        """.format(get_xp(message.author.id)))
        
    if message.content.lower().startswith('k!color'):
        color = random.randint(0, 0xFFFFFF)
        em = discord.Embed(title=hex(color), color=color)
        await client.send_message(message.channel, embed=em)
        
    if message.content == "k!help":
        embed = discord.Embed(title="My prefix: `k!`", description="**Commands:**", color=0xFF8C00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/442029742523416582/5dc70bc8a6d30c38a74c423dc3e8182e.png?size=1024")
        embed.add_field(name="hello", value="I greting you!", inline=False)
        embed.add_field(name="ping", value="I ping you!", inline=False)
        embed.add_field(name="lol", value="LOL!", inline=False)
        embed.add_field(name="xp", value="I write your xp!", inline=False)
        embed.add_field(name="vote", value="I create a vote!", inline=False)
        embed.add_field(name="invite", value="I write link to add me to your server!", inline=False)
        embed.add_field(name="help", value="I help you!", inline=False)
        embed.add_field(name="messages", value="I count your messages in this channel!", inline=False)
        embed.add_field(name="party", value="I send GIF", inline=False)
        embed.add_field(name="game_over", value="Game Over!", inline=False)
        embed.add_field(name="embed", value="I write a test of embed!", inline=False)
        embed.add_field(name="love", value="I love you!", inline=False)
        embed.add_field(name="color", value="I send random color!", inline=False)
        embed.add_field(name="game", value="I write what game you are playing", inline=False)
        await client.send_message(message.channel, embed=embed)
        

        


    if message.content.lower().startswith('k!vote'):
        em = discord.Embed(title="👍 or 👎?", color=random.randint(0, 0xFFFFFF))
        botem = await client.send_message(message.channel, embed=em)
        
        await client.add_reaction(botem, '👍')
        await client.add_reaction(botem, '👎')
        
    #if message.content.startswith("k!say"):
        #msg = message.replace("k!say"," ")
        #await client.say(msg)
            
    user_add_xp(message.author.id, 1)

def user_add_xp(user_id: int, xp: int):
    if os.path.isfile("users.json"):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['xp'] += xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['xp'] = xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {user_id: {}}
        users[user_id]['xp'] = xp
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_xp(user_id: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['xp']
    else:
        return 1

client.run(BOT_TOKEN)

