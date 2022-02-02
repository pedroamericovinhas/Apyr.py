from glob import glob
import os
from random import randint

def bible_verse():
    files = [file for file in glob("./bible_verses/*")]
    versiculo = files[randint(0, len(files)-1)]
    with open(versiculo, 'r', encoding="utf-16") as f:
        lines = [x for x in f.read().split("\n") if (x and not x.endswith(":"))]
    random_line = lines[randint(0, len(lines)-1)]
    title = f'{lines[0].split(", ")[0]} {lines[0].split(", ")[1]}:{random_line.split()[0][:-1]}'
    return title, " ".join(random_line.split()[1:])

bible_verse()