import discord
import json
import urllib
from random import randint, sample
from glob import glob

champs = []
games = []
global NC
NC = {"NC": 382635181997293568,
      "geral": 389605206586818570,
      "bots": 388848904281653248,
      "programming": 729823047342620753,
      }

global NCMEMBROS
NCMEMBROS = {
    "LUIZ":    185102910982586370,
    "DORO":    179412087154409472,
    "TUCO":    297905219491201024,
    "NATAN":   392182500270800906,
    "PIMENTA": 262992640310509570,
    "DIGAO":   298208982881796099,
}
global pimp_phrases
pimp_phrases = [
    "Hello , good hunter . I am a doll , here in this dream to look after you . Honourable hunter , pursue the echoes of blood and I will channel them into your strength . You will hunt beasts and I will be here for you , to embolden your sickly spirit .",
    "Farewell , good hunter . May you find your worth in the waking world .",
    "Very well , let the echoes become your strength . Let me stand close , now shut your eyes .",
    "Did you speak with Gehrman ? He was a hunter long , long ago . But now serves only to advise them . He is obscure , unseen in the dreaming world . Still , he stays here , in this dream . Such is his purpose ."
    "Ah , the little ones . Inhabitants of the dream , they find hunters like yourself , worship and serve them . Speak words they do not , but still , aren't they sweet ? ",
    "Over time , countless hunters have visited this dream . The graves here stand in their memory ... it all seems , so long ago now .",
    "Hunters have told me about the Church , about the Gods and their love . But , do the Gods love their creations . I am a doll created by you humans , would you ever think to love me ? Of course , I do love you , isn't that how you've made me ?"
    "Ah , welcome home , good hunter . I must have drifted off , what is it you desire ?"

]




with open("champions.json", encoding='utf-8') as f:
    data = json.load(f)
for i in data:
    champs.append(i["name"])

with open("steamgames.json", encoding='utf-8') as f:
    data = json.load(f)
for i in data["applist"]["apps"]:
    if ("OST" not in i['name'].upper() and
        "DLC" not in i['name'].upper() and
        "SOUNDTRACK" not in i['name'].upper() and
        "ADD-ON" not in i['name'].upper()):
        games.append(i)

def bible_verse():
    # Returns a bible verse's name and its contents

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


def lume222():
    while True:
        game = games[randint(0, len(games))]
        steamid = game["appid"]

        with urllib.request.urlopen(f"https://store.steampowered.com/api/appdetails?appids={steamid}") as url:
            data = json.loads(url.read().decode())[str(steamid)]

        if data["success"]:
            data = data["data"]
            if ("fullgame" not in data) and ("header_image" in data):
                print(f"Game {data['name']} found!")
                name = data["name"]
                templates = [f"ou bora jogar [{name}](https://store.steampowered.com/app/{steamid})",
                             f"nao nao bora jogar [{name}](https://store.steampowered.com/app/{steamid})",
                             f"ENTREM NO [{name.upper()}](https://store.steampowered.com/app/{steamid}) FILHAS DA PUTA"]
                embed = discord.Embed()
                embed.set_author(name="Lume222", icon_url="https://i.imgur.com/8ueszQt.png")
                embed.description = templates[randint(0, len(templates) - 1)]

                embed.set_image(url=data["header_image"])
                return embed
            else:
                print("game is DLC! trying again...", )
        else:
            print("game not found! trying again...")


def natan(natan_avatar):
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
    embed = discord.Embed()
    embed.set_author(name="É a vida p-p", icon_url=natan_avatar)
    embed.description = templates[randint(0, len(templates) - 1)] if randint(0,199) else "caarlho amno o veigar me deu 231k2ek k de danos kdas ewrek"
    return embed


def pimenta(sentence, pimp_pfp, pimp_name):
    new_sentence = []

    for word in sentence.split(" "):
        if len(word) == 1:
            new_sentence.append(word)
        else:
            new_sentence.append(f"{word[0]}{''.join(sample(word[1:-1], len(word[1:-1])))}{word[-1]}")
    embed = discord.Embed()
    embed.set_author(name=pimp_name, icon_url=pimp_pfp)
    embed.description = ' '.join(new_sentence)
    return embed


def digao(pfp_url, nick):
    title, desc = bible_verse()
    embed = discord.Embed(title=title, description=desc, color=0xffff80)
    embed.set_author(name=nick, icon_url=pfp_url)
    return embed


def thiago():
    pass