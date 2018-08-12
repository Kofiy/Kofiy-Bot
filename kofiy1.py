#https://discordapp.com/oauth2/authorize?client_id=457633173669412875&scope=bot&permissions=2146958847
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import json
import os.path
import random



BOT_PREFIX = "k!"
clientBot = Bot(command_prefix=BOT_PREFIX)

client = discord.Client()
BOT_TOKEN = "YYxxxxSECRET--TOKENxxxxYY"

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
@clientBot.command(pass_context=True)
async def say(ctx, * , message):
    await client.say( message)
    

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
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/436883644473409538/466926711448272899/trump.png",)

    if message.content == 'k!game_over':
        botmag = await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/465256769690796033/465941825597997066/triggered.gif")
    
        await client.add_reaction(botmag, '🆗')

    if message.content.lower().startswith('k!lol'):
        await client.send_message(message.channel, ":rofl: LOL :rofl: !")
        
   #if message.content.lower().startswith('k!server-invite'):
       #SInvite = await client.create_invite(message.channel, max_age="99999"
       #await client.send_message(message.channel,'{}' .format(SInvite))

    if message.content.lower().startswith('k!invite'):
        await client.send_message(message.channel, "`https://discordapp.com/oauth2/authorize?client_id=457633173669412875&scope=bot&permissions=2146958847`")

    if message.content.lower().startswith('k!party'):
        await client.send_message(message.channel, "https://giphy.com/gifs/carnaval-carnival-dance-10hO3rDNqqg2Xe")
        
    if message.content.lower().startswith('k!messages'):
        counter = 0
        tmp = await client.send_message(message.channel, "Calculating messages...")
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))


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
clientBot.run(BOT_TOKEN)
