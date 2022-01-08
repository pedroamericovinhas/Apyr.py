import os
import shutil
from datetime import datetime as dt
from glob import glob
from random import randrange

import discord
import requests
from mimesis import Internet

from download import *
from memes import *

client = discord.Client()


@client.event
async def on_ready():
    b = time.time()
    print(f'друг is online [took {int((b - a) * 1000)}ms]')


messages = ['', '']
stored = []


@client.event
async def on_message(message):
    content = message.content.split(" ")
    if message.guild is None:
        print(f"[{dt.now().strftime('%Y-%m-%d %H:%M:%S')}]{message.author} @ {message.channel.recipient} DM: {message.content}")
    else:
        print(f"[{dt.now().strftime('%Y-%m-%d %H:%M:%S')}]{message.author} @ {message.guild}(#{message.channel}): {message.content}")
    if message.author != client.user:
        messages.append(message)
        messages.pop(0)

    if message.author == client.user:
        return

    if '>help' in message.content:
        await message.channel.send(
            '''Comandos: 
            **>download** ***[url]*** Baixa um vídeo do Youtube e manda no chat como .mp4
            **>submit** ***[url]*** Baixa um vídeo no Youtube e guarda na pasta de memes do bot
            **>meme** Manda um meme aleatório da pasta de memes do bot
            **>natan** Simula uma frase que Natan falaria segundos depois de morrer no lol''')

    elif message.content == ">submit":
        for url in message.attachments:
            print(url.url)
            local_filename = url.url.split('/')[-1]
            r = requests.get(url, stream=True)
            with open("../memes/" + local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            await message.channel.send(f"Meme instalado! Temos {len(glob('../memes/*'))} memes na pasta")

    elif message.content.startswith('>download https://www.youtube.com/'):
        await message.channel.send('Vídeo sendo baixado...')
        urlDown(content[1])
        await message.channel.send('Vídeo sendo enviado...')
        vfile = max(glob('./*.mp4'), key=os.path.getctime) or "Error"
        await message.channel.send(file=discord.File(vfile))
        os.remove(vfile)

    elif message.content.endswith('.mp4') and message.content.startswith('>download https://'):
        await message.channel.send('Vídeo sendo baixado...')
        urlDown(content[1])
        await message.channel.send('Vídeo sendo enviado...')
        vfile = max(glob('./*.mp4'), key=os.path.getctime) or "Error"
        await message.channel.send(file=discord.File(vfile))
        os.remove(vfile)

    elif '>memes' in message.content:
        await message.channel.send(f"Temos `{len(glob('../memes/*'))}` memes na pasta")

    elif '>meme' in message.content:
        memes = glob('../memes/*')
        if randrange(0, 10):
            string = 'muito foda ' + randrange(4, 20) * 'k'
        else:
            string = 'muito foda ' + randrange(5, 9) * 'K'
        await message.channel.send(string)
        await message.channel.send(file=discord.File(memes[randrange(1, len(memes))]))

    elif message.content.startswith('>submit '):
        await message.channel.send('Vídeo sendo baixado...')
        urlDown(content[1])
        try:
            shutil.move(max(glob('./*.mp4'), key=os.path.getctime), '../memes/')
            await message.channel.send(f"Meme instalado! Temos `{len(glob('../memes/*'))}` memes na pasta")
        except shutil.Error:
            await message.channel.send('Meme já foi instalado!')
            os.remove(max(glob('./*.mp4'), key=os.path.getctime))

    elif message.content.startswith('>natan'):
        await message.channel.send(natan_rage())

    elif message.content.lower().startswith("delete"):
        await message.delete()

    elif message.content.lower() == "bad bot":
        rip = Internet().ip_v4()
        await message.author.send(rip)

    elif message.content.lower().startswith("send "):
        user = await client.fetch_user(int(content[1]))
        await user.send(' '.join(content[2:]))

with open("../client.txt") as f:
    x = f.read()

client.run(x)
