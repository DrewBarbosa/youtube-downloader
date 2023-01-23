from pytube import YouTube

SAVE_PATH = "" # Your destination file, remember to add double back slash \\. Example ("C:\\")


def download():
    global SAVE_PATH

    link = []

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
