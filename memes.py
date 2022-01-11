import json
from random import randint

import discord

champs = []
games = []
global NC
NC = {"geral": 389605206586818570,
      "bots": 388848904281653248,
      "programming": 729823047342620753, }


with open("champions.json", encoding='utf-8') as f:
    data = json.load(f)
for i in data:
    champs.append(i["name"])

with open("steamgames.json", encoding='utf-8') as f:
    data = json.load(f)
for i in data["applist"]["apps"]:
    if "OST" not in i['name'].upper() and "DLC" not in i['name'].upper():
        games.append(i)


def lume222():
    game = games[randint(0, len(games))]
    name = game["name"]
    steamid = game["appid"]

    templates = [f"ou bora jogar [{name}](https://store.steampowered.com/app/{steamid})",
                 f"nao nao bora jogar [{name}](https://store.steampowered.com/app/{steamid})",
                 f"ENTREM NO [{name.upper()}](https://store.steampowered.com/app/{steamid}) FILHAS DA PUTA"]
    embed = discord.Embed()
    embed.description = templates[randint(0, len(templates)-1)]
    return embed


def natan():
    damage = randint(800, 3000)
    champ = champs[randint(1, len(champs)-1)]
    skill = randint(1, 4)
    seconds = randint(1, 30)/10
    skills = ["Q", "W", "E"]
    lanes = ["top", "mid", "bot"]

    templates = [f"MANO {champ} me deu {damage} de dano em {skill} {skills[randint(0,2)]}",
                 f"cara {champ.lower()} literalmente me deu {damage} de dano em uma ult",
                 f"MANO {champ.upper()} ME DEU {damage} DE DANO EM {skill} FUCKING {skills[randint(0,2)].upper()}",
                 f"{champ.upper()} ME DEU {damage} DE DANO EM {seconds} SEGUNDOS KKKKKKKKKKKKKK",
                 f"{champ.upper()} ME DEU {damage} DE TRUE DAMAGE EM {seconds} SEGUNDOS?????????",
                 f"{randint(1,14)} min de jogo e essa merda de {champ.lower()} ja ta no {lanes[randint(0,2)]}??", ]

    return templates[randint(0, len(templates)-1)]
