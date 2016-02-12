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
  img, pozadina, marka_automobila = main.readFromFile(filename)
  ispis = 'Logo koji ste odabrali odgovara marki automobila: ' + marka_automobila
  label_tekst = Label(topFrame, text = ispis).pack(side = BOTTOM)
  
  #return img, pozadina, marka_automobila
  
#================================================================

root = Tk()
root.wm_title("Car logo detector")
root.minsize(width=600, height=400)
root.resizable(width=FALSE, height=FALSE)

#rad sa dugmetom za ucitavanje slike
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

button = Button(bottomframe, text="Učitaj logo", command = load_file)
button.pack( side = BOTTOM)

#podesi inicijalnu sliku pozadine
img = Image.open('car_logos.jpg')
tkImage = ImageTk.PhotoImage(img)
topFrame = Frame(root)
label_slika = Label(topFrame, image = tkImage).pack(side = TOP)
#trenutniLogoBrend = load_file().marka_automobila   

topFrame.pack(side = TOP)
       
root.mainloop()
