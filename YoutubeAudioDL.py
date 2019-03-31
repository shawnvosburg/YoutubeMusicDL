from tkinter import *
from pathlib import Path
import pytubedl as utubedl
from tkinter import filedialog


def show_entry_fields():
   print("Folder: %s\nURL: %s" % (e1.get(), e2.get()))

def setText(e,text):
    e.delete(0,END)
    e.insert(0,text)
    return

def download(labelText,folder,url):
    labelText.set("Status: DOWNLOADING")
    master.update_idletasks()
    utubedl.DownloadYT(folder,url)
    labelText.set("Status: SUCCESS")
    master.update_idletasks()
    

#===================================================================================
#Build GUI
#===================================================================================
master = Tk()
master.title("YoutubeAudioDL - By: Shawn Vosburg")
Label(master, text="Folder").grid(row=0,sticky=W)
Label(master, text="YoutubeURL").grid(row=1,sticky=W)

#Set default value for Songs
MusicFolder = str(Path.home()) + str("\Music")
e1 = Entry(master,width = 50)
e2 = Entry(master,width = 50)

e1.grid(row=0, column=1)
e1.insert(END,MusicFolder)
e2.grid(row=1, column=1)

labelText = StringVar()
labelText.set("Status: WAITING")
L1 = Label(master,textvariable=labelText).grid(row=2,column=1, sticky=W, pady=4)

Button(master, text='Folder', command=lambda : setText(e1,filedialog.askdirectory())).grid(row=0,column=2, sticky=W, pady=4)
Button(master, text='DOWNLOAD', command=lambda : download(labelText,e1.get(),e2.get())).grid(row=1, column=2, sticky=W, pady=4)


mainloop( )