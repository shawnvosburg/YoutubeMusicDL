from __future__ import unicode_literals
import youtube_dl
import os
from sys import argv
import ffmpeg

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

#Get directory from config file
with open('config.txt') as f:
    for line in f:
        task = line.split(':')
        if(task[0] == "Download"):
            dir = task[1]

# Song Directory
if not os.path.exists(dir):
	os.mkdir(dir)
else:
	os.chdir(dir)

# Download Songs
with youtube_dl.YoutubeDL(download_options) as dl:
	dl.download([argv[1]])