from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk

type_file = (("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All Files", "*.*"))

def showImage():
  global type_file
  fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=type_file)
  print("Image path :", fln)
  img = Image.open(fln)
  img = ImageTk.PhotoImage(img)
  lbl.configure(image=img)
  lbl.image = img


root = Tk()

frm = Frame(root)
frm.pack(side=BOTTOM, padx=15, pady=15)

lbl = Label(root)
lbl.pack()

btn = Button(frm, text="Browse Image", command=showImage)
btn.pack(side=tk.LEFT)

btn2 = Button(frm, text="Exit", command=lambda: exit())
btn2.pack(side=tk.LEFT, padx=10)

root.title("Image Broser App")
root.geometry("500x400")
root.mainloop()
