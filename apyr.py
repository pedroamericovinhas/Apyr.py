from download import *
import os
import shutil
from datetime import datetime as dt
from glob import glob
from random import randrange, randint
import datetime

import discord
import requests
from mimesis import Internet
from discord.ext import tasks
import discord.utils

from memes import *
from loggers import logga
client = discord.Client()

intents = discord.Intents.default()

@client.event
async def on_ready():
    global NerdCrew
    b = time.time()
    print(f'друг is online [took {int((b - a) * 1000)}ms]')


@tasks.loop(seconds=58)
async def timekeeping():
    now =  datetime.datetime.now().time()
    t_0222 = datetime.time(2,  22)
    t_0223 = datetime.time(2,  23)
    t_2220 = datetime.time(22, 20)
    t_2221 = datetime.time(22, 21)
    if (t_0222 <= now <= t_0223) or (t_2220 <= now <= t_2221):
        print("message sent!")
        Luiz = await client.fetch_user(NCMEMBROS["LUIZ"])
        await Luiz.send("<:lume222:927640120616702033>")


@client.event
async def on_message(message):
    programming = await client.fetch_channel(NC["programming"])
    content = message.content.split(" ")

    logga(message)

    try:
        if message.channel == programming and "github" in message.content.split('/')[-3]:
            await message.pin()
    except IndexError:
        pass

    if message.author == client.user:
        return
    if '>help' in message.content:
        with open('help.txt', 'r', encoding="utf-8") as f:
            await message.channel.send(f.read())

    elif message.type == discord.MessageType.pins_add:
        await message.delete()

    elif message.content == ">pimenta":
        nerdcrew = await client.fetch_guild(NC["NC"])
        PIMENTA = await nerdcrew.fetch_member(NCMEMBROS["PIMENTA"])
        pimp_avatar = PIMENTA.avatar_url
        pimp_name = PIMENTA.nick if PIMENTA.nick else PIMENTA.name
        msg = message
        if message.reference:
            msg = await message.channel.fetch_message(message.reference.message_id)
            await message.channel.send(embed=pimenta(msg.content,pimp_avatar, pimp_name))
        else:
            await message.channel.send(embed=pimenta(pimp_phrases[randrange(0, len(pimp_phrases))],pimp_avatar, pimp_name))

    elif message.content.startswith('>natan'):
        nerdcrew = await client.fetch_guild(NC["NC"])
        NATAN = await nerdcrew.fetch_member(NCMEMBROS["NATAN"])
        natan_avatar = NATAN.avatar_url
        await message.channel.send(embed=natan(natan_avatar))

    elif message.content == ">submit":
        msg = message
        if message.reference:
            msg = await message.channel.fetch_message(message.reference.message_id)
        for url in msg.attachments:
            local_filename = url.url.split('/')[-1].split(".")
            r = requests.get(url, stream=True)
            with open("../memes/" + local_filename[0] + str(randint(10000, 99999)) + '.' + local_filename[-1], 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            await message.channel.send(f"Meme instalado! Temos {len(glob('../memes/*'))} memes na pasta")

    elif message.content.startswith(">ideia ") or message.content.startswith(">idea "):
        with open('./ideias.txt', 'a', encoding="utf-8") as f:
            f.write(f"[{dt.now().strftime('%Y-%m-%d %H:%M:%S')}] {message.author}: {' '.join(content[1:])}\n")
            await message.channel.send(
                "nossos trabalhadores assalariados (pedro) irão tomar conta da sua sugestão :slight_smile:")

    elif message.content.startswith(">ideias"):
        embed = discord.Embed()
        with open('./ideias.txt', 'r', encoding="utf-8") as f:
            embed.description = f.read()
        await message.channel.send(embed=embed)

    elif message.content.startswith('>download https://www.youtube.com/'):
        await message.channel.send('Vídeo sendo baixado...')
        yt_down(content[1])
        await message.channel.send('Vídeo sendo enviado...')
        vfile = max(glob('./*.mp4'), key=os.path.getctime) or "Error"
        await message.channel.send(file=discord.File(vfile))
        os.remove(vfile)

    elif message.content.endswith('.mp4') and message.content.startswith('>download https://'):
        await message.channel.send('Vídeo sendo baixado...')
        yt_down(content[1])
        await message.channel.send('Vídeo sendo enviado...')
        vfile = max(glob('./*.mp4'), key=os.path.getctime) or "Error"
        await message.channel.send(file=discord.File(vfile))
        os.remove(vfile)

    elif '>memes' in message.content:
        await message.channel.send(f"Temos `{len(glob('../memes/*'))}` memes na pasta")

    elif '>meme' in message.content:
        memes = glob('../memes/*')
        string = 'muito foda ' + randint(4, 12) * 'k' if randint(0, 10) else 'muito foda ' + randint(5, 10) * 'K'
        await message.channel.send(file=discord.File(memes[randrange(1, len(memes))]), content=string)

    if message.content.lower().startswith(">digao") or message.content.lower().startswith(">digão"):
        nerdcrew = await client.fetch_guild(NC["NC"])
        DIGAO = await nerdcrew.fetch_member(NCMEMBROS["DIGAO"])
        digao_pfp = DIGAO.avatar_url
        digao_name = DIGAO.nick if DIGAO.nick else DIGAO.name
        await message.channel.send(embed=digao(digao_pfp, digao_name))

    elif message.content.startswith('>submit '):
        await message.channel.send('Vídeo sendo baixado...')
        yt_down(content[1])
        try:
            shutil.move(max(glob('./*.mp4'), key=os.path.getctime), '../memes/')
            await message.channel.send(f"Meme instalado! Temos `{len(glob('../memes/*'))}` memes na pasta")
        except shutil.Error:
            await message.channel.send('Meme já foi instalado!')
            os.remove(max(glob('./*.mp4'), key=os.path.getctime))

    elif message.content.lower().startswith("delete"):
        await message.delete()

    elif message.content.lower() == "bad bot":
        rip = Internet().ip_v4()
        await message.author.send(rip)

    elif message.content.lower().startswith("send "):
        user = await client.fetch_user(int(content[1]))
        await user.send(' '.join(content[2:]))
    elif message.content.lower().startswith("sendchannel "):
        channel = await client.fetch_channel(int(content[1]))
        await channel.send(' '.join(content[2:]))

    elif message.content.lower().startswith(">lume222"):
        await message.channel.send(embed=lume222())

    elif message.content.lower() == "widepeepohappy":
        await message.channel.send("<:wide:901309342693859409><:peepo:901309342559653940><:happy:901309342509301801>")
        await message.delete()

    elif message.content.lower().startswith(">troll "):
        try:
            user = await client.fetch_user(int(content[1]))
            await user.send("<:tf:851224502721445988>")
        except:
            channel = await client.fetch_channel(int(content[1]))
            await channel.send("<:tf:851224502721445988>")

    elif message.content.lower().startswith(">pin"):
        pins = await message.channel.pins()
        msg = pins[randint(0, len(pins)-1)]
        if msg.attachments:
            attach = msg.attachments[0]
            local_filename = attach.url.split('/')[-1]
            r = requests.get(attach.url, stream=True)

            with open("./coisas/" + local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)

            await message.channel.send(file=discord.File(max(glob('./coisas/*'), key=os.path.getctime)), content=msg.content)
            os.remove(max(glob('./coisas/*'), key=os.path.getctime))
        else:
            await message.channel.send(msg.content)


timekeeping.start()

with open("../client.txt") as f:
    x = f.read()

client.run(x)