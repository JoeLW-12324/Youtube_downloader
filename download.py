"""This module contains functions for button commands which are used to download videos, audios, etc"""
# importing modules
from pytube import YouTube
from tkinter import messagebox

# function to download the video
def download_video(url, lbls, resolution, filename, path):
    try:
        video = search_video(url, lbls, resolution, downloading=True)
        if video is None:
            messagebox.showerror(title="Resolution unavailable", message="The resolution you have picked is invalid!")
        else:
            filename = None if filename == "" else f"{filename}.mp4" # check if the name entry is empty so it will set the default name to the video title
            download_now = video.download(filename=filename, output_path=path)
            messagebox.showinfo(title="Video downloaded!" ,message=f"Your file is saved in {download_now}")
    except Exception as e: # raise error box if link not found or invalud link
        messagebox.showerror(title="Youtube link not found", message="The link you have input is invalid!")

# function to download the audio
def download_audio(url, lbls, filename, path):
    try:
        yt = YouTube(url)
        video = yt.streams
        lbls[0]["text"] = "Video: " + slice(yt.title)
        lbls[1]["text"] = "Channel: " + yt.author
        downloaded_audio = video.get_audio_only()
        file_size = downloaded_audio.filesize
        lbls[2]["text"] = "file size: " + calculate_size(file_size)
        filename = None if filename == "" else f"{filename}.mp4"
        download_now = downloaded_audio.download(filename=filename, output_path=path)
        messagebox.showinfo(title="Audio downloaded!", message=f"Your file is saved in {download_now}")
    except Exception as e:  # raise error box if link not found or invalud link
        messagebox.showerror(title="Youtube link not found", message="The link you have input is invalid!")

# function to make sure the filename input isn't empty
def callback(var):
    if var.get() == " ":
        var.set("")


# function to properly format the title of the video if the title is long
def slice(title):
    if len(title) >= 30:
        title = title[:30] + "\n" + title[30:]
    return title

# function to calculate the file size and format it into MB, GB, etc
def calculate_size(bytes):
    if bytes >= 1000 and bytes  < 1000000:
        file_size = str(bytes  / 1000) + " KB"
    elif bytes  >= 1000000 and bytes  < 1000000000:
        file_size = str(bytes  / 1000000) + " MB"
    elif bytes  >= 1000000000:
        file_size = str(bytes / 1000000000) + " GB"
    else:
        file_size = str(bytes ) + " bytes"
    return file_size

# function to search the video and fill in the title and channel name
# it will return the youtube object if downloading is True ( for download now button command)
def search_video(url, lbls, resolution, downloading=False):
    try:
        yt = YouTube(url)
        video_stream = yt.streams
        lbls[0]["text"] = "Video: " + slice(yt.title)
        lbls[1]["text"] = "Channel: " + yt.author
        try:
            downloaded_video = video_stream.get_by_resolution(resolution)
            file_size = downloaded_video.filesize
            lbls[2]["text"] = "File size: " + calculate_size(file_size)
        except Exception as e:
            lbls[2]["text"] = "File size: File unavailable"
            messagebox.showerror(title="Resolution unavailable", message="The resolution you have picked is invalid!")
            return None
        if downloading:
            return downloaded_video
    except Exception as e:  # raise error box if link not found or invalud link
        messagebox.showerror(title="Youtube link not found", message="The link you have input is invalid!")