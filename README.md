# Youtube downloader 

This is a Youtube downloader GUI made from tkinter and
python using the pytube package. 

This project contains three files, the main.py files is where everything 
will be run mainly. The download.py file contains functions used for the button commands 
and are mainly used to download the youtube video or audio. The path_selection.py 
file is used to select and create path where the downloaded videos and audio are send to. 

You are require to install the pytube package to use this application as it is used to find the youtube 
video and download it as a mp4 file format. 

To download videos, copy and insert a youtube video link into the link entry. You can click on the search button to 
check on the video's title, channel and filesize. You can select the video resolution from 
144p to 720p but some video resolution are unavailable for download and the program will show you an error message 
when you click on the download or search button 

You can start downloading videos by clicking on the "Download Now" button which will download the video in the resolution you have selected 
and name it to a certain name that you have input, if you do not put any name for the file, the file name will be the video title as its default. 
During downloading, the app will freeze for a few seconds until the video is fully downloaded and the program will show a message saying that your video is fully downloaded. 
After downloading, the video is sent to the path that the user select. 

You can also download video audio by clicking on the "Download Audio" button. Just like downloading a video, you can name 
the audio by putting in a name in the file name entry and choose which path to put the downloaded audio too. 

Finally, the user can name their file by putting in a name in the "File name" entry, if the entry is empty, the downloaded file will contain the same name 
as the video title. When a video or audio is downloaded, the file is usually send to the C:/Youtube downloader/downloaded path, which the program will create if it does not exist yet. 
However, the user is able to select their own path by clicking the "Select path" button which will open a file dialog where the user can search for a path where the files will be sent to. 


