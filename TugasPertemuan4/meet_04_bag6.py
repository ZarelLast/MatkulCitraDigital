import tkinter

window = tkinter.Tk()
window.title("Belajar GUI Python Meet 04 Part 4")

def left_click(e):
  tkinter.Label(window, text="Left Click!").pack()

def middle_click(e):
  tkinter.Label(window, text="Middle Click!").pack()

def right_click(e):
  tkinter.Label(window, text="Right Click!").pack()

window.bind("<Button-1>", left_click)
window.bind("<Button-2>", middle_click)
window.bind("<Button-3>", right_click)

window.mainloop()