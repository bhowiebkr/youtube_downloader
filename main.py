import sys
import os
import youtube_dl


def main():

    music_folder = os.path.join(os.getenv("HOME"), "Music")
    if not os.path.exists(music_folder):
        os.makedirs(music_folder)

    URL = sys.argv[1]

    params = {
        "format": "bestaudio/best",
        "outtmpl": music_folder + "/%(uploader)s/%(title)s.%(ext)s",
        "ignoreerrors": True,
    }

    with youtube_dl.YoutubeDL(params=params) as ydl:
        ydl.extract_info(URL, download=True)


if __name__ == "__main__":
    main()
