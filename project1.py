import numpy as np
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *



# This part of the code will just simply focus on the homepage
# or what the user first sees when they load the game
# It will contain the basic instructions of how to play the game
# And it will contain a button.
# When the user presses that button the game will start


# PART I - TKINTER GUI
myWindow = Tk()
myWindow.title("Computer Graphics")
myWindow.geometry('1440x900')
myWindow['background'] = '#BE8C5B'

load = Image.open('Images\\gameBackground1.jpg')
render = ImageTk.PhotoImage(load)
img = Label(myWindow, image=render)
img.place(x=0, y=0)

title1 = Label(myWindow, text="Welcome to Turtle-Rex", bg="#A5C146", fg="white", font="Ravie 30 bold")
title2 = Label(myWindow, text="Can your turtle win?", bg="#A5C146", fg="white", font="Calibri 15 italic")

title3 = Label(myWindow, text="The game is simple. Your turtle will", bg="#A5C146",  fg="white", font="Calibri 15 bold italic")
title3a = Label(myWindow, text="have to complete the race", bg="#A5C146",  fg="white", font="Calibri 15 bold italic")
title3b = Label(myWindow, text="Using different controls you can control", bg="#A5C146", fg='white', font="Calibri 15 bold italic")

title4a = Label(myWindow, text="the direction of where your turtle is headed", bg="#A5C146", fg='white',  font="Calibri 15 bold italic")
title4b = Label(myWindow, text="Click Start when you are ready. Have fun!", bg="#A5C146",  fg="white", font="Calibri 15 bold italic")


# Since this is just the homepage
# all the tkinter widgets will be put on to the myWindow page by using place
title1.place(x=400, y=100)
title2.place(x=620, y=170)
title3.place(x=490, y=300)
title3a.place(x=490, y=330)
title3b.place(x=490, y=360)
title4a.place(x=490, y=390)
title4b.place(x=490, y=415)

# Currently the button is not interactive as it has no command
# The method to be called when the button is pressed is implemented later
gameGenerator = Button(myWindow, text="Start", bg='#A5C146', fg='white', font="Ravie 10")
gameGenerator.place(x=735, y=460)
gameGenerator. config(width=10)

myWindow.mainloop()