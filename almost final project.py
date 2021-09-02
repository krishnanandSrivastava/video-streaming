import tkinter as tk
import requests
from tkinter import *
import tkinter
from tkinter import messagebox
from lib2to3.fixer_util import Number
import urllib.request
import urllib.parse
import re
import vlc,pafy
import tkinter as tk
from PIL import Image, ImageTk
import easygui
HEIGHT = 450
WIDTH = 800

root = tk.Tk()
root.title("Youtube")
root.maxsize(800,450)
root.minsize(800,450)
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

def helloCallBack():
    query_string = urllib.parse.urlencode({"search_query" : entry.get()})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    #print("http://www.youtube.com/watch?v=" + search_results[0])
    c="http://www.youtube.com/watch?v=" + search_results[0]
    media =c
    url=c
    video=pafy.new(url)
    best=video.getbest()
    media=vlc.MediaPlayer(best.url)
    media.play()
    def play():
        media.play()
    def stop():
        media.stop()
    def pause():
        media.pause()
    def again():
        media.stop()
        helloCallBack()
    button6 = tk.Button(frame, text="Search", font=40, command=again)
    button6.place(relx=0.7, relheight=1, relwidth=0.3)
    lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.51, relheight=0.13, anchor='n')
    label = tk.Label(lower_frame)
    label.place(relwidth=1, relheight=1)
    button2 = tk.Button(lower_frame, text="play", font=40, command= play, padx=35)
    button2.grid(row=0, column=1)
    button3 = tk.Button(lower_frame, text="pause", font=40, command= pause, padx=35)
    button3.grid(row=0, column=2)
    button4 = tk.Button(lower_frame, text="close", font=40, command= stop, padx=35)
    button4.grid(row=0, column=3)
    #root.destroy()
  
background_image = tk.PhotoImage(file='y.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Search", font=40, command=helloCallBack)
button.place(relx=0.7, relheight=1, relwidth=0.3)



root.mainloop()
