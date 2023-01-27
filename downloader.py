from pytube import YouTube
import os

SAVE_PATH = f"C:\\Users\\{os.getlogin()}\\Desktop\\yt-downloader"


def download():
    global SAVE_PATH

    link = ["https://www.youtube.com/watch?v=-VFG-Tp6QvE"]

    if link == [] or link == None:
        return print("No video to download")

    for i in link:
        try:
            yt = YouTube(i)
        except:
            print("Connection Error")

        try:
            print("Downloading video...")
            yt.streams.filter(progressive=True, file_extension='mp4').order_by(
                'resolution').desc().first().download(SAVE_PATH)
        except:
            print("Some Error!")
    print("Task Completed!")
    link = ""

download()