import tkinter

window = tkinter.Tk()
window.title("Belajar GUI Python Meet 04 Part 7")

icon = tkinter.PhotoImage(file="./TugasPertemuan4/res/btn.png")

label = tkinter.Label(window, image=icon)
label.pack()

window.mainloop()