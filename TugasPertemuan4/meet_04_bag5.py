import tkinter

window = tkinter.Tk()
window.title("Belajar GUI Python Meet 04 Part 4")
counter = 0

def say_hi(e):
  global counter
  output_txt = str(f"Hi you click me {counter} times(s)")
  tkinter.Label(window, text=output_txt).pack()
  counter += 1

btn = tkinter.Button(window, text="Click me!")
btn.bind("<Button-1>", say_hi)
btn.pack()

window.mainloop()