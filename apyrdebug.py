import time
a = time.time()
import discord
import json
import urllib
from random import randint, sample
import asyncio
from glob import glob
NC = {"NC": 382635181997293568,
      }
NCMEMBROS = {
    "DIGAO": 298208982881796099
}


client = discord.Client()

with open("bible.txt", "r", encoding="utf-16") as f:
    biblia = f.read()


@client.event
async def on_ready():
    global NerdCrew
    b = time.time()
    print(f'друг is online [took {int((b - a) * 1000)}ms]')

def bible_verse():
    # Returns a bible verse's name and its contents

    # Gets all the paths for the files in ./bible_verses/ , then
    # chooses a random one
    files = [file for file in glob("./bible_verses/*")]
    versiculo = files[randint(0, len(files)-1)]

    # Opens the file and removes empty lines and lines ending with `:`
    # (To avoid lines such as "And then God said:")
    with open(versiculo, 'r', encoding="utf-16") as f:
        lines = [x for x in f.read().split("\n") if (x and not x.endswith(":"))]

    # Formats the title and content and returns both as a tuple
    random_line = lines[randint(0, len(lines)-1)]
    title = f'{lines[0].split(", ")[0]} {lines[0].split(", ")[1]}:{random_line.split()[0][:-1]}'
    return title, " ".join(random_line.split()[1:])


def digao(pfp_url, nick):
    title, desc = bible_verse()
    embed = discord.Embed(title=title, description=desc, color=0xffff80)
    embed.set_author(name=nick, icon_url=pfp_url)
    return embed


@client.event
async def on_message(message):
    if message.content.lower().startswith(">lume222"):
        embed = lume222()
        await message.channel.send(embed=embed)
        print("")
    if message.content.lower().startswith(">digao") or message.content.lower().startswith(">digão"):
        nerdcrew = await client.fetch_guild(NC["NC"])
        DIGAO = await nerdcrew.fetch_member(NCMEMBROS["DIGAO"])
        digao_pfp = DIGAO.avatar_url
        digao_name = DIGAO.nick if DIGAO.nick else DIGAO.name
        await message.channel.send(embed=digao(digao_pfp, digao_name))


with open("../client.txt") as f:
    x = f.read()

client.run(x)