import tkinter

window = tkinter.Tk()
window.title("Belajar Gui Python Meet 04 Part 3")

tkinter.Label(window, text="Username").grid(row=0)
tkinter.Entry(window).grid(row=0, column=1)

tkinter.Label(window, text="Password").grid(row=1)
tkinter.Entry(window).grid(row=1, column=1)

tkinter.Checkbutton(window, text="Keep me Signed In").grid(columnspan=2)

lbl_img = tkinter.PhotoImage(file="./TugasPertemuan4/res/btn.png")
tkinter.Button(window, image=lbl_img, borderwidth=0).grid(columnspan=2)

window.mainloop()