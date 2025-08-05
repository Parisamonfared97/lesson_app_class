from tkinter import *
from tkinter import messagebox
from tkinter import ttk

lesson_list=[]

def ok_click():
    pass
def edit_click():
    pass
def remove_click():
    pass



window = Tk()
window.title("Lessons Info")
window.geometry("700x400")
window.resizable(False, False)

#Code
code=IntVar()
Label(window, text="code").place(x=20, y=60)
Entry(window, textvariable=code).place(x=80, y=60)

#Title
title=StringVar()
Label(window, text="Title").place(x=20, y=100)
Entry(window, textvariable=title).place(x=80, y=100)

#
# #Teacher
teacher=StringVar()
Label(window, text="Teacher").place(x=20, y=140)
Entry(window, textvariable=teacher).place(x=80, y=140)


# #Class Number
class_num=IntVar()
Label(window, text="Number").place(x=20, y=180)
Entry(window, textvariable=class_num).place(x=80, y=180)


#unit
unit=IntVar()
Label(window, text="Unit").place(x=20, y=220)
Entry(window, textvariable=unit).place(x=80, y=220)


#Buttons
Button(window, text="Ok", command=ok_click).place(x=80, y=300)
Button(window, text="Ok", command=edit_click).place(x=80, y=300)
Button(window, text="Ok", command=remove_click).place(x=80, y=300)





window.mainloop()