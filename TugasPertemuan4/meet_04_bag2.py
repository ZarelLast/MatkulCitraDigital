import tkinter

window = tkinter.Tk()
window.title("Belajar GUI Python Meet 04 Part 2")

tkinter.Label(window, text="Suf. Width", fg="white", bg="purple").pack()
tkinter.Label(window, text="Taking all available x width", fg="white", bg="green").pack(fill="x")
tkinter.Label(window, text="Talomg all available y width", fg="white", bg="black", width="50").pack(side="left", fill="y")

window.mainloop()
