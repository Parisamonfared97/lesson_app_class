from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3

lesson_list=[]

def reset_form():
    code.set(0)
    title.set("")
    teacher.set("")
    class_num.set(0)
    unit.set(0)

def save_click():
    lessons={
    "code":code.get(),
    "title":title.get(),
    "teacher":teacher.get(),
    "class_num":class_num.get(),
    "unit":unit.get()
    }
    lesson_list.append(lessons)
    messagebox.showinfo("save",f"Class Saved Successfully!\n{lessons}")
    reset_form()
    table.insert("",END,values=tuple(lessons.values()))

selected_row_id = None

def select_lesson(event):
    global selected_row_id
    selected_row_id=table.focus()
    selected_lesson=table.item(selected_row_id)["values"]
    code.set(selected_lesson[0])
    title.set(selected_lesson[1])
    teacher.set(selected_lesson[2])
    class_num.set(selected_lesson[3])
    unit.set(selected_lesson[4])


def edit_click():
    global selected_row_id
    if selected_row_id :
        updated_lesson={
            "code":code.get(),
            "title":title.get(),
            "teacher":teacher.get(),
            "class_num":class_num.get(),
            "unit":unit.get()
        }
        table.item(selected_row_id,values=tuple(updated_lesson.values()))
        index=table.index(selected_row_id)
        lesson_list[index] = updated_lesson
        messagebox.showinfo("edit",f"Class Edited Successfully!\n{updated_lesson}")
        reset_form()
        selected_row_id=None
    else:
        messagebox.showerror("error","No Lesson Selected")

def remove_click():
    pass



window = Tk()
window.title("Class Info")
window.geometry("700x370")
window.resizable(False, False)

img=Image.open("dars.jpg")
img=ImageTk.PhotoImage(img)
window.iconphoto(window,img)


#Code
code=IntVar()
Label(window, text="Code").place(x=20, y=20)
Entry(window, textvariable=code).place(x=90, y=20)

#Title
title=StringVar()
Label(window, text="Title").place(x=20, y=60)
Entry(window, textvariable=title).place(x=90, y=60)

#
# #Teacher
teacher=StringVar()
Label(window, text="Teacher").place(x=20, y=100)
Entry(window, textvariable=teacher).place(x=90, y=100)
lesson=StringVar()


# #Class Number
class_num=IntVar()
Label(window, text="Number").place(x=20, y=140)
Entry(window, textvariable=class_num).place(x=90, y=140)


#unit
unit=IntVar()
Label(window, text="Unit").place(x=20, y=180)
Entry(window, textvariable=unit).place(x=90, y=180)


#Buttons
Button(window, text="Save", command=save_click,width=7).place(x=20, y=300)

Button(window, text="Edit", command=edit_click,width=7).place(x=90, y=300)

Button(window, text="Remove", command=remove_click,width=7).place(x=160, y=300)

#search by class title
search_title=StringVar()
Label(window, text="Search Title:").place(x=250, y=20)
Entry(window, textvariable=search_title).place(x=320, y=20)


#search by teacher
search_teacher=StringVar()
Label(window, text="Search Teacher:").place(x=450, y=20)
Entry(window, textvariable=search_teacher).place(x=540, y=20)

#Table
table=ttk.Treeview(window,height=12,columns=("Code","Title","Teacher","Class","Unit"),show="headings")
table.column("Code", width=82)
table.column("Title", width=82)
table.column("Teacher", width=82)
table.column("Class", width=82)
table.column("Unit", width=82)

table.heading("Code", text="Code")
table.heading("Title", text="Title")
table.heading("Teacher", text="Teacher")
table.heading("Class", text="Class")
table.heading("Unit", text="Unit")

table.bind("<<TreeviewSelect>>", select_lesson)
table.place(x=252,y=60)

window.mainloop()