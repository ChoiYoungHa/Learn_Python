from tkinter import *

window = Tk()

# 윈도우 프로그래밍 글자위치, 글자색, 배경색 조정
label1 = Label(window, text="PYTHON을")
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="blue")
label3 = Label(window, text="공부중입니다.", bg="magenta", width=20, height=5, anchor=NE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()
