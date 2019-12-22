import youtube_dl
import os

DOWNLOAD_TYPE = "audio"  # audio / video
URL = "https://www.youtube.com/watch?v=zJGvJtE94tY"


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == "nt":
        import winreg

        sub_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
        downloads_guid = "{374DE290-123F-4565-9164-39C4925E467B}"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser("~"), "downloads")


def main():

    params = {
        "format": "bestaudio/best",
        "outtmpl": get_download_path() + os.sep + "%(title)s.%(ext)s",
        "ignoreerrors": True,
    }

    if DOWNLOAD_TYPE == "video":
        params["format"] = "bestvideo+bestaudio"

    with youtube_dl.YoutubeDL(params=params) as ydl:
        data = ydl.extract_info(URL, download=True)


if __name__ == "__main__":
    main()
