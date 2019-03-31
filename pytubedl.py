from __future__ import unicode_literals
import youtube_dl
import os
from sys import argv
import ffmpeg

def DownloadYT(dir,url):
    # Download data and config
    download_options = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'nocheckcertificate': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    # Song Directory
    if not os.path.exists(dir):
        os.mkdir(dir)
        os.chdir(dir)
    else:
        os.chdir(dir)

    # Download Songs
    with youtube_dl.YoutubeDL(download_options) as dl:
        dl.download([url])