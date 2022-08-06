# Importing modules
from tkinter import *
from download import download_video, download_audio, callback, search_video
from path_selection import create_path, select_path

# the default path used where videos are downloaded to
output_path = create_path()

# main function to create and run the GUI
def main(name):
    # creating GUI
    root = Tk()
    root.geometry("500x400")
    root.resizable(0, 0)
    root.title("Youtube downloader")
    root.iconbitmap('youtube.ico')

    # options
    resolution_options = ["720p", "480p", "360p", "240p", "144p"]

    # Label
    title_lbl = Label(root, text="Youtube downloader", fg="red", font=("Verdana bold" ,20)).place(x=100, y=0)
    link_lbl = Label(root, text="Link:", font=("Times", 15)).place(x=65, y=42)
    resolution_lbl = Label(root, text="Resolution:", font=("Times bold", 10)).place(x=140, y=124)
    vid_title_lbl = Label(root, font=("Times", 10))
    vid_title_lbl.place(x=30, y=150)
    author_lbl = Label(root, font=("Times", 10))
    author_lbl.place(x=40, y=190)
    size_lbl = Label(root, font=("Times", 10))
    size_lbl.place(x=40, y=220)
    name_lbl = Label(root, text="File name:", font=("Times", 15)).place(x=45, y=260)
    path_lbl = Label(root, text="Path:", font=("Times", 15)).place(x=45, y=300)

    # creating string var and entry
    link = StringVar()
    name = StringVar()
    name.trace("w", lambda x, index, mode: callback(name)) # need to fill in 3 arguments for unknown reason
    clicked = StringVar(value=resolution_options[0])
    current_path = StringVar(value=output_path)
    url = Entry(root, textvariable=link, bd=2, width=50) # entry for user to input url link
    url.place(x=120, y=45)
    file_naming = Entry(root, textvariable=name, bd=1, width=30) # entry for user to input file name
    file_naming.place(x=140, y=265)
    path_entry = Entry(root, textvariable=current_path, bd=1,width=50) # path entry
    path_entry.place(x=100, y=305)
    path_entry.configure(state='disabled')

    # resolution options
    reso_drop = OptionMenu(root, clicked, *resolution_options).place(x=220, y=120)

    # button
    search_btn = Button(root, text="Search",
                        command=lambda: search_video(link.get(), (vid_title_lbl, author_lbl, size_lbl), clicked.get()))
    search_btn.place(x=250, y=80)
    download_btn = Button(root, text="Download Now",
                          command=lambda:download_video(link.get(), (vid_title_lbl, author_lbl, size_lbl),
                                                        clicked.get(), name.get(), current_path.get()))
    download_btn.place(x=200, y=340)
    download_audio_btn = Button(root, text="Download Audio",
                                command=lambda:download_audio(link.get(), (vid_title_lbl, author_lbl, size_lbl),
                                                              name.get(),  current_path.get()))
    download_audio_btn.place(x=320, y=340)
    path_btn = Button(root, text="Select Path", command=lambda:select_path(current_path))
    path_btn.place(x=100, y=340)

    # running GUI
    mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
