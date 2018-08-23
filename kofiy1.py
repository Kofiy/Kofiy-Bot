#https://discordapp.com/oauth2/authorize?client_id=457633173669412875&scope=bot&permissions=2146958847
import asyncio
import os.path
import random
import simplejson as json
import discord
from discord import ext
from discord import embeds
from discord import Embed
from discord.embeds import EmptyEmbed
import requests
from discord import user
from discord import utils
from discord import client
from discord.client import Client
from discord.utils import snowflake_time
from discord.user import User
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot

BOT_PREFIX = "k!"
client = Bot(command_prefix=BOT_PREFIX)
BOT_TOKEN = "TOKEN"

 #This is for me
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='k!help'))
    print("-------------------")
    print("""
Hello! I'm ready 
    """)
#commands

@client.command
async def test():
    await client.send_message(message.channel, "test!!!")
    await client.delete_message("k!test")


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
        await client.delete_message(message)
        await client.add_reaction(botmag, '🆗')

    if message.content.lower().startswith('k!lol'):
        await client.delete_message(message)
        await client.send_message(message.channel, ":rofl: LOL :rofl: !")
        
   #if message.content.lower().startswith('k!server-invite'):
       #SInvite = await client.create_invite(message.channel, max_age="99999"
       #await client.send_message(message.channel,'{}' .format(SInvite))

    if message.content == 'k!info':
        invite = discord.Embed(color=random.randint(0, 0xFFFFFF))
        invite.set_author(name="Kofiy Bot", url="https://discord.gg/aXzh2uD", icon_url="https://cdn.discordapp.com/avatars/442029742523416582/5dc70bc8a6d30c38a74c423dc3e8182e.png?size=1024")
        invite.add_field(name="My creator:", value="Kofiy#7248", inline=False)
        invite.add_field(name="My ID:", value="457633173669412875", inline=False)
        invite.add_field(name="Invite me:", value="https://discordapp.com/oauth2/authorize?client_id=457633173669412875&scope=bot&permissions=2146958847", inline=False)
        await client.send_message(message.channel, embed=invite)

    if message.content.lower().startswith('k!party'):
        party = discord.Embed(color=0x12AD4F)
        party.set_image(url="https://giphy.com/gifs/carnaval-carnival-dance-10hO3rDNqqg2Xe")
        await client.delete_message(message)
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
        await client.delete_message(message)


    if message.content.lower().startswith('k!xp'):
        await client.send_message(message.channel, """```css
You have {} XP!```
        """.format(user_get_xp(message.author.id)))
        
    if message.content.lower().startswith('k!color'):
        color = random.randint(0, 0xFFFFFF)
        em = discord.Embed(title=hex(color), color=color)
        await client.send_message(message.channel, embed=em)
        
    if message.content == "k!help":
        respone = random.randint(1, 5)
        if respone == 1:
            e = discord.Embed(title="Wait please...")
        if respone == 2:
            e = discord.Embed(title="Moment...")
        if respone == 3:
            e = discord.Embed(title="Wait!")
        if respone == 4:
            e = discord.Embed(title="Loading...")
        if respone == 5:
            e = discord.Embed(title="...")
        e.set_footer(text="1 second")
        m = await client.send_message(message.channel, embed=e)

        asyncio.sleep(250)
        await client.delete_message(m)

        em = discord.Embed(title="""My prefix: `k!`
Commands:""", color=0xFF8C00)
        em.set_author(name="Kofiy Bot", url="https://discord.gg/aXzh2uD", icon_url="https://cdn.discordapp.com/avatars/442029742523416582/5dc70bc8a6d30c38a74c423dc3e8182e.png?size=1024")
        em.set_footer(text="""Click to "Kofiy Bot".""")
        em2 = discord.Embed(title="Utility & Info", color=0x5A009D)
        em2.set_thumbnail(url="http://rm-london.co.uk/blog/wp-content/uploads/2015/12/Info-image-830x530.png")
        em2.add_field(name="xp", value="I write your xp!", inline=False)
        em2.add_field(name="vote", value="I create a vote!", inline=False)
        em2.add_field(name="info", value="I send info about me.", inline=False)
        em2.add_field(name="help", value="I help you!", inline=False)
        em2.add_field(name="messages", value="I count your messages in this channel!", inline=False)
        em2.add_field(name="game", value="I write what game you are playing", inline=False)
        em3 = discord.Embed(title="Fun & Other", color=0x00FF00)
        em3.set_thumbnail(url="https://cdn.pixabay.com/photo/2015/04/04/19/02/fun-706870_960_720.jpg")
        em3.add_field(name="hello", value="I greting you!", inline=False)
        em3.add_field(name="ping", value="I ping you!", inline=False)
        em3.add_field(name="lol", value="LOL!", inline=False)
        em3.add_field(name="party", value="I send GIF", inline=False)
        em3.add_field(name="game_over", value="Game Over!", inline=False)
        em3.add_field(name="embed", value="I write a test of embed!", inline=False)
        em3.add_field(name="love", value="I love you!", inline=False)
        em3.add_field(name="color", value="I send random color!", inline=False)
        em3.set_footer(text="Help given to {0.author.name}." .format(message))
        
        await client.send_message(message.channel, embed=em)
        await client.send_message(message.channel, embed=em2)
        await client.send_message(message.channel, embed=em3)
        

        


    if message.content.lower().startswith('k!vote'):
        em = discord.Embed(title="👍 or 👎?", color=random.randint(0, 0xFFFFFF))
        botem = await client.send_message(message.channel, embed=em)
        
        await client.add_reaction(botem, '👍')
        await client.add_reaction(botem, '👎')
        
    #if message.content.startswith("k!say"):
        #msg = message.replace("k!say"," ")
        #await client.say(msg)
            
    user_add_xp(message.author.id)

def user_add_xp(user_id: int, xp: int):
    if os.path.isfile("xp.json"):
        try:
            with open('xp.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['xp'] += xp
            with open('xp.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('xp.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['xp'] = xp
            with open('xp.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {user_id: {}}
        users[user_id]['xp'] = xp
        with open('xp.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_xp(user_id: int):
    if os.path.isfile('xp.json'):
        with open('xp.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['xp']
    else:
        return 1


client.run(BOT_TOKEN)
