import time

print("друг is initializing")
a = time.time()

from yt_dlp import YoutubeDL

ydl_opts = {'format': 'mp4',
            'quiet': False,
            'noplaylist': True}


def yt_down(link):
    url = "https://www.youtube.com/watch?v=" + link[27:38] if "shorts" in link else link
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
