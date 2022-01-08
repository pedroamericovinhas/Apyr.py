import json
from random import randint

champs = []

with open("champions.json", encoding='utf-8') as f:
    data = json.load(f)
for i in data:
    champs.append(i["name"])


def natan_rage():
    damage = randint(800, 3000)
    champ = champs[randint(1, len(champs)-1)]
    skill = randint(1, 4)
    seconds = randint(1, 30)/10
    skills = ["Q", "W", "E"]
    templates = [f"MANO {champ} me deu {damage} de dano em {skill} {skills[randint(0,2)]}",
                 f"cara {champ.lower()} literalmente me deu {damage} de dano em uma ult",
                 f"MANO {champ.upper()} ME DEU {damage} DE DANO EM {skill} FUCKING {skills[randint(0,2)].upper()}",
                 f"{champ.upper()} ME DEU {damage} DE DANO EM {seconds} SEGUNDOS KKKKKKKKKKKKKK",
                 f"{champ.upper()} ME DEU {damage} DE TRUE DAMAGE EM {seconds} SEGUNDOS?????????", ]
    return templates[randint(0, len(templates)-1)]
