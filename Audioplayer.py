#importing required modules & libraires
from tkinter import *
import pygame
import os


window=Tk()
window.geometry("1000x200+220+200")  #window geometry
window.title("Audio Player") #Title of the window

pygame.mixer.init() #Initiating Pygame Mixer
window.track=StringVar() #Declaring track variable
window.status=StringVar() #Declaring status variable

def play(): #Defining Play Song Function
    song_name=window.track.set(window.playlist.get(ACTIVE))
    pygame.mixer.music.load(window.playlist.get(ACTIVE))
    pygame.mixer.music.play()
    window.status.set("-Playing")
    print("playing")

def pause(): #Defining Pause Song Function
    pygame.mixer.music.pause()
    window.status.set("-Paused")
    print("paused")

trackframe = LabelFrame(window,text="Song Track",font=("times new roman",15,"bold"),bg="black",fg="Yellow",bd=5,relief=GROOVE) #Creating Track Frame for Song label & status label
trackframe.place(x=0,y=100,width=600,height=100)

songtrack = Label(trackframe,textvariable=window.track,width=20,font=("times new roman",24,"bold"),bg="black",fg="yellow").grid(row=0,column=0,padx=10,pady=5)#Inserting Songtrack Label
trackstatus = Label(trackframe,textvariable=window.status,font=("times new roman",24,"bold"),bg="black",fg="yellow").grid(row=0,column=10,padx=10,pady=5)#Inserting Status Label
#Creating Button Frame
buttonframe = LabelFrame(window,text="Buttons",font=("times new roman",15,"bold"),bg="black",fg="yellow",bd=5,relief=GROOVE)
buttonframe.place(x=0,y=0,width=600,height=100)

b2=Button(buttonframe,text="PLAY",command=play,width=15,height=1,font=("times new roman",22,"bold"),fg="black",bg="yellow").grid(row=5,column=3,padx=7,pady=2)#Creating play button
b3=Button(buttonframe,text="Pause",command=pause,width=15,height=1,font=("times new roman",22,"bold"),fg="black",bg="yellow").grid(row=5,column=6,padx=7,pady=2)#Creating pause button
#Creating Playlist Frame
songs_listbox = LabelFrame(window,text="Playlist",font=("times new roman",15,"bold"),bg="black",fg="yellow",bd=5,relief=GROOVE)
songs_listbox.place(x=600,y=0,width=400,height=200)
    
scrol_y = Scrollbar(songs_listbox,orient=VERTICAL)#Inserting scrollbar
    
window.playlist = Listbox(songs_listbox,yscrollcommand=scrol_y.set,selectbackground="yellow",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="black",fg="yellow",bd=5,relief=GROOVE)#Inserting Playlist listbox
#Applying Scrollbar to listbox
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=window.playlist.yview)
window.playlist.pack(fill=BOTH)

#Fetching Audios
song_list = os.listdir()
#Inserting Audios into Playlist
for track in song_list:
    window.playlist.insert(END,track)

window.mainloop()
