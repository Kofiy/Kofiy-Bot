import asyncio
import urllib
import inspect
from bs4 import BeautifulSoup
import os.path
import random
import time
import timeit
import datetime
import discord
import PIL
import requests
import simplejson as json
from discord.ext import commands
from discord.ext.commands import Bot
from PIL import Image, ImageChops, ImageOps
from io import BytesIO, StringIO
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

BOT_PREFIX = "k!"
client = commands.Bot(command_prefix='!')
BOT_TOKEN = "<TOKEN HERE>"




@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="k@help | I am on {} servers!" .format(len(client.servers)), type=2))
    print("-------------------")
    print("""
Hello! I'm ready
    """)


@client.event
async def on_message(message):
  
    if message.content.startswith('k#invert'):
        string = message.content

        text = string.split(' ')
        for word in text:
            if word == "k#invert" or word == '':
                url = None
            else:
                url = word
                response = requests.get(url)
                img = Image.open(BytesIO(response.content))
                img.save("img.png")
                image = Image.open('img.png')
                inverted = PIL.ImageOps.invert(image)
                inverted.save('invert.png')
                await client.send_file(message.channel, "invert.png")

    if message.content.startswith('k!hello'):
        language = get_lang(message.server.id)
        if language == 1:
            msg = 'Привет {0.author.mention}!'.format(message)
        if language == 2:
            msg = 'Hello {0.author.mention}!'.format(message)
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('k!ping'):
        msg = '**{0.author.mention} Pong!**'.format(message)
        await client.send_message(message.channel, msg)

    if message.content == 'k!embed':
        embed = discord.Embed(title="Title", description="This is a __test__ `embed`", color=0x00ff00)
        await client.send_message(message.channel, embed=embed)


    if message.content == 'k?game':
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

    if message.content == 'k@info':
        invite = discord.Embed(color=random.randint(0, 0xFFFFFF))
        invite.set_author(name="Kofiy Bot", url="https://discord.gg/aXzh2uD", icon_url="https://cdn.discordapp.com/avatars/442029742523416582/5dc70bc8a6d30c38a74c423dc3e8182e.png?size=1024")
        invite.add_field(name="Bot Version:", value="1.2.0", inline=False)
        invite.add_field(name="My creator:", value="Kofiy#7248", inline=False)
        invite.add_field(name="My ID:", value="457633173669412875", inline=False)
        invite.add_field(name="Invite me:", value="https://discordapp.com/oauth2/authorize?client_id=457633173669412875&scope=bot&permissions=2146958847", inline=False)
        invite.add_field(name="My Server:", value="https://discord.gg/aXzh2uD", inline=False)
        await client.send_message(message.channel, embed=invite)

    if message.content == "k@ping" or message.content == "k?ping":
        await client.delete_message(message)
        before = time.monotonic()
        pong = discord.Embed(title="Pong!", color=random.randint(0, 0xFFFFFF))
        message = await client.send_message(message.channel, embed=pong)
        ping = (time.monotonic() - before) * 1000
        pong = discord.Embed(title=f"Pong {int(ping)}ms!", color=random.randint(0, 0xFFFFFF))
        await client.edit_message(message, embed=pong)
        print(f'Ping {int(ping)}ms')

    if message.content.lower().startswith('k?messages'):
        counter = 0
        wait = discord.Embed(title="Calculating messages...")
        tmp = await client.send_message(message.channel, embed=wait)
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        counmes = discord.Embed(title="You have {} messages.".format(counter), color=random.randint(0, 0xFFFFFF))
        await client.edit_message(tmp, embed=counmes)
        await client.delete_message(message)


    if message.content.lower().startswith('k?xp'):
        await client.send_message(message.channel, """```css
You have {} XP!```
        """.format(get_xp(message.author.id)))

    if message.content.lower().startswith('k.set_description'):
        if message.author.server_permissions.manage_channel:
            __id = message.content.split(' ')
            __des = message.content.split('"')
            _ID = __id[1]
            _DES = __des[1]

        await client.edit_channel(client.get_channel(_ID), topic=_DES)

    if message.content.startswith('k?add_reaction'):
        __args = message.content.split(' ')
        _CHAN = __args[1]
        _MES = __args[2]
        _ID = __args[3]
        for emoji in client.get_all_emojis():
            if emoji.id == _ID:
                await client.add_reaction(client.get_message(client.get_channel(_CHAN), str(_MES)), emoji)

    if message.content.lower().startswith('k!color'):
        color = random.randint(0, 0xFFFFFF)
        hex__ = hex(color)
        hex_ = hex__.split('0x')
        _HEX = hex_[1]
        em = discord.Embed(title="#" + _HEX, color=color)
        await client.send_message(message.channel, embed=em)

    if message.content.startswith('k!say'):
        string = message.content
        text = string.split("k!say ")
        for word in text:
            if word == '':
                return
            else:
                teax = word
                if teax.startswith('k!say') or teax.endswith('k!say') or teax.startswith('@everyone') or teax.endswith('@everyone'):
                    await client.send_message(message.channel, "No, i don't say this!")
                else:
                    await client.send_message(message.channel, teax)
                    await client.delete_message(message)

    if message.content.startswith('k?profil'):
        await client.delete_message(message)
        if True:
            if True:
                try:
                    member_ping = message.content.split(' ')[1]
                    member_id = member_ping.split('<')[1][1:19]
                    _MEMBER = message.server.get_member(member_id)
                except IndexError:
                    _MEMBER = message.author
                    
                from PIL import ImageFont, ImageDraw, Image

                image = Image.open("Assets/bg/{}.jpg" .format(random.randint(1, 5)))

                draw = ImageDraw.Draw(image)
                font = ImageFont.truetype("Assets/Lobster-Regular.ttf", 66)
                print(_MEMBER.name)
                draw.text(((image.size[0] / 2) - (font.getsize(_MEMBER.name)[0] / 2), (image.size[1] / 2) - (image.size[1] / 5)), _MEMBER.name, font=font, fill=(0, 0, 0, 125))
                font = ImageFont.truetype("Assets/Lobster-Regular.ttf", 64)
                draw.text(((image.size[0] / 2) - (font.getsize(_MEMBER.name)[0] / 2), (image.size[1] / 2) - (image.size[1] / 5)), _MEMBER.name, font=font)

                xp = get_xp(_MEMBER.id)
                font = ImageFont.truetype("Assets/Lobster-Regular.ttf", 66)
                print(message.author.name)
                draw.text(((image.size[0] / 4) - (font.getsize("XP: {}" .format(xp))[0] / 2), (image.size[1] / 2) + 5), "XP: {}" .format(xp), font=font, fill=(0, 0, 0, 125))
                font = ImageFont.truetype("Assets/Lobster-Regular.ttf", 64)
                # print(message.author.name)
                draw.text(((image.size[0] / 4) - (font.getsize("XP: {}" .format(xp))[0] / 2), (image.size[1] / 2) + 5), "XP: {}" .format(xp), font=font)

                image.save('Assets/result.png', 'PNG')

                await client.send_file(message.channel, "Assets/result.png", filename="{}RankCard.png" .format(_MEMBER.name))

    if '@everyone' in message.content or '@here' in message.content:
        for z in client.get_all_emojis():
            if z.id == "502811524180606976":
                await client.add_reaction(message, z)

    if message.content.startswith('k?video-stats'):
                a = list(message.content.split('video-stats ')[1])
                i = 0
                while i < len(a):
                    if a[i] == ' ':
                        a[i] = '%20'
                    i = i + 1
                b = ''.join(a)
                url = 'https://www.abonixapi.ga/YoutubeStats.php?url={}' .format(b)

                data = extract_data(url).split(':')
                tit = data[1].replace('Views', '')
                vie = data[2].replace('Likes', '')
                like = data[3].replace('Dislikes', '')
                dis = data[4].replace('Comments', '')
                com = data[5].replace('Thumbnail URL', '')
                thum = data[6].replace('Video length', '')
                v_len = data[7] + ':' + data[8]
                print(thum)
                print(v_len)
                
                em = discord.Embed(title=tit)
                em.add_field(name="Views:", value=vie, inline=True)
                em.add_field(name="Likes:", value=like, inline=True)
                em.add_field(name="Dislikes:", value=dis, inline=True)
                em.add_field(name="Comments Count:", value=com, inline=True)
                em.set_footer(text="Powered by https://www.abonixapi.ga/YoutubeStats.php")
                await client.send_message(message.channel, embed=em)
    if message.content == 'k!joke':
        url = 'https://www.abonixapi.ga/RandomJoke.php'
        text = extract_data(url)

        joke = discord.Embed(title=text, color=random.randint(0, 0xffffff))
        joke.set_footer(text="Powered by https://www.abonixapi.ga/RandomJoke.php")

        await client.send_message(message.channel, embed=joke)

    if message.content == 'k#gradient':
        url = 'https://www.abonixapi.ga/RandomJoke.php'
        data = extract_data(url).split('"')
        col1 = data[3]
        col2 = data[7]
        grad = data[11]

        gradient = discord.Embed(title="{} <=> {}" .format(col1, col2))
        gradient.set_thumbnail(url=grad)

        await client.send_message(messsage.channel, embed=gradient)

        joke = discord.Embed(title=text, color=random.randint(0, 0xffffff))
        joke.set_footer(text="Powered by https://www.abonixapi.ga/RandomJoke.php")
        await client.send_message(message.channel, embed=joke)

    if message.content.startswith('k?cool_text'):
        await client.delete_message(message)
        a = list(message.content.split('k?cool_text ')[1])
        i = 0
        print(len(a))
        while i < len(a):
            if a[i] == ' ':
                a[i] = '%20'
            i = i + 1
            print(i)
        print(a)
        b = ''.join(a)

        print(b)
        url = "https://www.abonixapi.ga/CoolFont.php?text={}" .format(b)
        text = extract_data(url)
        em = discord.Embed(title=text, color=random.randint(0, 0xffffff))
        em.set_footer(text="Powered by https://www.abonixapi.ga/CoolFont.php")
        await client.send_message(message.channel, text)
        
    if message.content.startswith("k@help"):
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

        asyncio.sleep(500)
        await client.delete_message(m)
        em = discord.Embed(title="""Fun prefix:`k!`
Info prefix: `k@`
Utils prefix: `k?`
Moderator prefix: `k.`
Music prefix: `k+`""", color=0xFF8C00)
        em.set_author(name="Kofiy Bot", url="https://discord.gg/aXzh2uD", icon_url="https://cdn.discordapp.com/avatars/442029742523416582/5dc70bc8a6d30c38a74c423dc3e8182e.png?size=1024")
        em.set_footer(text="""Click to "Kofiy Bot".""")
        em2 = discord.Embed(title="Info", description="`k@`", color=0x5A009D)
        uti = discord.Embed(title="Utils", description="`k?`", color=0xFA0000)
        em2.set_thumbnail(url="http://rm-london.co.uk/blog/wp-content/uploads/2015/12/Info-image-830x530.png")
        uti.add_field(name="profil {user @mention}", value="I get user rank card!", inline=False)
        uti.add_field(name="vote", value="I create a vote!", inline=False)
        uti.add_field(name="video-stats { url }", value="I get a stats of video!", inline=False)
        uti.add_field(name="ping", value="Pong!", inline=False)
        em2.add_field(name="info", value="I send info about me.", inline=False)
        em2.add_field(name="help", value="I help you!", inline=False)
        em2.add_field(name="modules", value="I write the modules!", inline=False)
        em2.add_field(name="ping", value="Pong!", inline=False)
        uti.add_field(name="messages", value="I count your messages in this channel!", inline=False)
        uti.add_field(name="game", value="I write what game you are playing", inline=False)
        em3 = discord.Embed(title="Fun", description="`k!`", color=0x00FF00)
        uti.add_field(name="cool_text { text }", value="I write a cool text! (!!!Don't use cyrilic leters!!!)", inline=False)
        em3.set_thumbnail(url="https://cdn.pixabay.com/photo/2015/04/04/19/02/fun-706870_960_720.jpg")
        em3.add_field(name="hello", value="I greting you!", inline=False)
        em3.add_field(name="ping", value="I ping you!", inline=False)
        em3.add_field(name="lol", value="LOL!", inline=False)
        em3.add_field(name="game_over", value="Game Over!", inline=False)
        em3.add_field(name="embed", value="I write a test of embed!", inline=False)
        em3.add_field(name="love", value="I love you!", inline=False)
        em3.add_field(name="color", value="I send random color!", inline=False)
        em3.add_field(name="joke", value="I say a joke!", inline=False)
        mod = discord.Embed(title="Moderator", description="`k.`", color=0xFADD09)
        mus = discord.Embed(title="Music", description="`k+`",)
        mod.add_field(name="new-channel", value="I create a channel!", inline=False)
        mus.add_field(name="ON DEVELOP", value="on develop", inline=False)
        mus.set_footer(text="Help given to {0.author.name}." .format(message))
        cmd = message.content
        await client.send_message(message.channel, embed=em)
        if cmd == "k@help info" or cmd == "k@help Info" or cmd == "k@help INFO" or cmd == "k@help инфо" or cmd == "k@help Information":
            await client.send_message(message.channel, embed=em2)
        else:
            if cmd == "k@help UTILS" or cmd == "k@help utils" or cmd == "k@help Utils" or cmd == "k@help утилиты":
                await client.send_message(message.channel, embed=uti)
            else:
                if cmd == "k@help Fun" or cmd == "k@help fun" or cmd == "k@help FUN" or cmd == "k@help веселье" or cmd == "k@help funny":
                    await client.send_message(message.channel, embed=em3)
                else:
                    if cmd == "k@help Moderator" or cmd == "k@help moderator" or cmd == "k@help MODERATOR" or cmd == "k@help модератор":
                        await client.send_message(message.channel, embed=mod)
                    else:
                        if cmd == "k@help music" or cmd == "k@help Music" or cmd == "k@help MUSIC" or cmd == "k@help музыка" or cmd == "k@help Melody":
                            await client.send_message(message.channel, embed=mus)
                        else:
                            moduleerror = discord.Embed(title="Wrong module!", description="Write `k@modules`", color=0xFF0000)
                            await client.send_message(message.channel, embed=moduleerror)
    if message.content == "k@modules":
        modules = discord.Embed(title="""
1. - Music/Melody
2. - Info
3. - Fun/Funny
4. - Moderator
5. - Utils
        """, color=0xFFAADD)
        await client.send_message(message.channel, embed=modules)


    if message.content.startswith('k$eval') and message.author.id in bot_suports:
        error = None
        await client.delete_message(message)
        lang = message.content.split(' ')[1]
        command = message.content.split('k$eval {} ' .format(lang))[1]
        if lang == 'py' or lang == 'python' or lang == 'ру' or lang == 'питон':
            try:
                res = eval(command)
                if inspect.isawaitable(res):
                    result = await res
                else:
                    result = res

                e = discord.Embed(title="EVAL Command", color=0x028cff)
                e.add_field(name=":inbox_tray: Command: ", value="""```python
{}```""" .format(command), inline=False)
                e.add_field(name=":outbox_tray: Return: ", value="```{}```" .format(result), inline=False)

                me = await client.send_message(message.channel, embed=e)
                await client.add_reaction(me, '🇪') 
                await client.add_reaction(me, '🇻')
                await client.add_reaction(me, '🇦')
                await client.add_reaction(me, '🇱')
            except Exception as e:
                error = str(e)

                e = discord.Embed(title="EVAL Command", color=0x028cff)
                e.add_field(name=":inbox_tray: Command: ", value="""```python
{}```""" .format(command), inline=False)
                e.add_field(name="<:Error:515621923791831051> Error: ", value="```{}```" .format(error), inline=False)
                me = await client.send_message(message.channel, embed=e)
                await client.add_reaction(me, '🇪') 
                await client.add_reaction(me, '🇻')
                await client.add_reaction(me, '🇦')
                await client.add_reaction(me, '🇱')
        elif lang == 'js' or lang == 'javascript' or lang == 'йс' or lang == 'джаваскрипт':
            await client.send_message(message.channel, "Sorry, but JavaScript is not suported")
        else:
            await client.send_message(message.channel, "Sorry, but {} is not suported" .format(lang))



    if True:
        user_add_xp(message.author.id, 1)

    if message.content.lower().startswith('k?vote'):
        v = message.content.split(' ')
        votetext = v[1]
        em = discord.Embed(title=votetext, description="👍 or 👎?", color=random.randint(0, 0xFFFFFF))
        botem = await client.send_message(message.channel, embed=em)
        like = 0
        dislike = 0
        await client.add_reaction(botem, '👍')
        await client.add_reaction(botem, '👎')
        while True:
            reaction = await client.wait_for_reaction(emoji=['👍', '👎'])
            if reaction.reaction.emoji == '👍':
                like += 1
                em = discord.Embed(title=votetext, description="""
**За** проголосовали {} человек.
**Против** проголосовали {} человек.
                """ .format(like, dislike), color=random.randint(0, 0xFFFFFF))
            if reaction.reaction.emoji == '👎':
                dislike += 1
                em = discord.Embed(title=votetext, description="""
**За** проголосовали {} человек.
**Против** проголосовали {} человек.
                """ .format(like, dislike), color=random.randint(0, 0xFFFFFF))
                await client.edit_message(botem, embed=em)    
