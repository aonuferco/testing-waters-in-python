import os
from tkinter import *
from tkinter import filedialog
from pytube import YouTube


def default_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path


def dir_change():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    progress.set("")


def yt_dw():
    try:
        progress.set("Accessing YouTube URL...")
        ys = YouTube(url.get())
        ys.streams.filter(file_extension='mp4').get_lowest_resolution().download(folder_path.get())
        progress.set("Download complete")

    except:
        progress.set("Error. Check your connection or URL")


# window
root = Tk()
root.geometry("550x100")
root.title("python Youtube Downloader")
root.resizable(False, False)

# labels and entry box
url = StringVar()
folder_path = StringVar()
folder_path.set(default_path())
progress = StringVar()

url_label = Label(root, text="Enter the YouTube video URL").grid(row=0, column=0)
url_entry = Entry(root, textvariable=url, width=50, bd=4).grid(row=0, column=1)
dir_label = Label(root, text="Your video will be saved to: ").grid(row=1, column=0)
dir_directory = Label(root, textvariable=folder_path).grid(row=1, column=1)
progress_label = Label(root, textvariable=progress).grid(row=2, column=1)

# buttons
url_button = Button(root, text="OK", command=yt_dw, width=10).grid(row=0, column=2)
dir_button = Button(root, text="Change", command=dir_change, width=10).grid(row=1, column=2)

root.mainloop()
