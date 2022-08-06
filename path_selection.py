"""This module is used to create the path and select path where
the videos downloaded will be put into """

# importing modules
from tkinter import filedialog
import os


# leaf directory
directory = "downloaded"
# Parent directories
parent_dir = "C:/Youtube downloader"

# default path for this program
path = os.path.join(parent_dir, directory)

# creating a path when user run the program for the first time and return the path to the main file
# to have it as the default path where videos are save
def create_path():
    try:
        os.makedirs(path, exist_ok=True)
        return path
    except Exception as e:
        return

# function to allow user to select a path they want their videos to be downloaded to
def select_path(var):
    #allows user to select a path from the explorer
    finding_path = filedialog.askdirectory()
    finding_path = path if finding_path == "" else finding_path # setting path back to the default path if user did not select path
    # set stringvar to path
    var.set(finding_path)