# -*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import Image, ImageTk
import cv2
import main

#================================================================
#funcionalnosti

def load_file():
  filename = askopenfilename(parent = root)
  img, pozadina = main.readFromFile(filename)
  #pozadina za sad ne radi, zamislio sam da se na pozadini prikazuje slika koja se dobija kao rezultat
  
#================================================================

root = Tk()
root.wm_title("Car logo detector")
root.minsize(width=600, height=400)
root.resizable(width=FALSE, height=FALSE)

#podesi inicijalnu sliku pozadine
img = Image.open('car_logos.jpg')
tkImage = ImageTk.PhotoImage(img)
topFrame = Frame(root)
label = Label(topFrame, image = tkImage).pack(side = TOP)
topFrame.pack(side = TOP)

#rad sa dugmetom za ucitavanje slike
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

button = Button(bottomframe, text="Učitaj sliku", command = load_file)
button.pack( side = BOTTOM)
            
root.mainloop()
