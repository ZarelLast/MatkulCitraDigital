from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk
import cv2 as cv
import numpy as np

root = Tk()

frm = Frame(root)
frm.pack(side=BOTTOM, padx=20, pady=20)

lbl = Label(root)
lbl.pack()

type_file = (("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All Files", "*.*"))
img_path = ''

def TampilImage(path):
  global lbl
  img = ImageTk.PhotoImage(path.resize((500,400), Image.ANTIALIAS))
  lbl.configure(image=img)
  lbl.image = img

def showImage():
  global img_path

  fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=type_file)
  img_path = np.copy(fln)
  img = Image.open(fln)
  TampilImage(img)

def redColor(img):
  img[:, :, 1] = 0
  img[:, :, 2] = 0
  return img

def greenColor(img):
  img[:, :, 0] = 0
  img[:, :, 2] = 0
  return img

def blueColor(img):
  img[:, :, 0] = 0
  img[:, :, 1] = 0
  return img

def imgLayer(color):
  img = cv.imread(str(img_path))
  (red, green, blue) = cv.split(cv.cvtColor(img, cv.COLOR_BGR2RGB))
  if color == 'red':
    img = Image.fromarray(red)
  elif color == 'green':
    img = Image.fromarray(green)
  else:
    img = Image.fromarray(blue)
  TampilImage(img)

btn = Button(frm, text="Browse", command=showImage)
btn.pack(side=tk.LEFT)

btnLR = Button(frm, text="Red", command=lambda: imgLayer('red'))
btnLR.pack(side=tk.LEFT, padx=5)

btnLG = Button(frm, text="Green", command=lambda: imgLayer('green'))
btnLG.pack(side=tk.LEFT, padx=5)

btnLB = Button(frm, text="Blue", command=lambda: imgLayer('blue'))
btnLB.pack(side=tk.LEFT, padx=5)

btnE = Button(frm, text="Exit", command=lambda: exit())
btnE.pack(side=tk.LEFT, padx=5)

root.title("Image Browser App - 5200411416")
root.geometry("500x400")
root.mainloop()