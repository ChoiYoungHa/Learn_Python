from tkinter import *

window = Tk()

photo = PhotoImage(file="../gif/이미지 019.png")
label1 = Label(window, image=photo)

label1.pack()

window.mainloop()

