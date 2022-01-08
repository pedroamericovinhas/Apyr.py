import time
print("друг is initializing")
a = time.time()
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch
from time import sleep
ydl_opts = {'format': 'mp4',
            'quiet': False,
            'noplaylist': True}
def urlDown(link):
    url = link
    if "shorts" in link:
        url = "https://www.youtube.com/watch?v=" + link[27:38]
    with YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
    pass    
  
def queryResults(query):
    info = YoutubeSearch(query, max_results=5).to_dict()
    return query


def searchVideo(query):
    if "https://www.youtube.com/watch?v=" in query:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(query)
            print('Video Downloaded.')
        pass
    else:
        info = YoutubeSearch(query, max_results=5).to_dict()
        while True:
            print("\nVideo selection. Type the video number to continue.\n")
            for i, video in enumerate(info, start=1):
                video["no"] = i
                sleep(0.05)
                print(f"{video.get('no')}. {video.get('title')} - {video.get('duration')}")
            selected = (input("\n"))
            if int(selected) not in range(1, 6):
                print(f"please input a number between 1 and {5}.")
                sleep(1)
                pass
            break
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download("https://www.youtube.com/watch?v=" + info[int(selected)-1].get('id'))    	
            print('Video Downloaded.')


if __name__ == '__main__' :
    searchVideo("teste")

