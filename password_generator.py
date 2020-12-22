from tkinter import *
from tkinter import font
import random
from tkinter import messagebox
import pyperclip

#function to create the password..
def output():
    weak = "abcdefghijklmnopqrstuvwxyzABCDEFGHiJKLMNOPQRSTUVWXYZ"
    medium = "abcdefghijklmnopqrstuvwxyzABCDEFGHiJKLMNOPQRSTUVWXYZ1234567890"
    strong = "abcdefghijklmnopqrstuvwxyzABCDEFGHiJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    try:
        length = numb.get()
        password_type = radio.get()
    except:
        messagebox.showerror("Input Error","please enter invalid input")
    if password_type == 0:
        password = "".join(random.sample(weak,length))
    elif password_type == 1:
        password = "".join(random.sample(medium,length))
    else:
        password = "".join(random.sample(strong,length))

    password_entry.delete(0,END)
    password_entry.insert(length,str(password))
#function to copy the password..
def copy():
    random_password = password_entry.get()
    pyperclip.copy(random_password)
# window to diplay the objects
master = Tk()
master.geometry("600x300")
master.title("Password Generator")
master.resizable(False,False)
master.config(background='#111')
#heading for window..
heading_text = Label(master,text = "Password Generator:",justify="center",fg="crimson",bg="#111",width=30,bd=0,font = font.Font(family="Helvetica",size =20),pady="10px")
heading_text.pack()
description_text = Label(master,text = "It will displays the various password according to your option..",fg="#fff",bg='#111',font=font.Font(family="Helvetica",size =12),bd=0)
description_text.pack()
#creating frame for inputs
input_frame = Frame(master,bg="#111")
input_frame.pack()
passwordd = StringVar()
numb = IntVar()
radio = IntVar()
password_label = Label(input_frame,text="Password :",fg="#fff",bg="#111",pady=15,padx=5,font=font.Font(family="Helvetica",size=14))
password_label.grid(row=0,column=0)
password_entry = Entry(input_frame,width=50,textvariable=passwordd)
password_entry.grid(row=0,column=1,padx=5,pady=5,columnspan=2)
copy_label = Button(input_frame,text="Copy",fg="#fff",bg="crimson",width=10,bd=0,command=copy)
copy_label.grid(row=0,column=3,padx=5,pady=5)
length_text=Label(input_frame,text="Length :",fg="#fff",bg="#111",font=font.Font(family="Helvetica",size=14))
length_text.grid(row=1,column=0,padx=0)
length_entry=Entry(input_frame,width=50,textvariable=numb,bg="#fff")
length_entry.grid(row=1,column=1,columnspan=2,padx=0)
type_text=Label(input_frame,text="Type :",fg="#fff",bg="#111",font=font.Font(family="Helvetica",size=14),padx=0,pady=10)
type_text.grid(row=2,column=0)
weak_radio=Radiobutton(input_frame,text="Weak",variable=radio,value=0,fg="slateblue",bg="#111",font=font.Font(family="Helvetica",size=12),activebackground="#111",activeforeground="crimson")
medium_radio=Radiobutton(input_frame,text="Medium",variable=radio,value=1,fg="slateblue",bg="#111",font=font.Font(family="Helvetica",size=12),activebackground="#111",activeforeground="crimson")
strong_radio=Radiobutton(input_frame,text="Strong",variable=radio,value=2,fg="slateblue",bg="#111",font=font.Font(family="Helvetica",size=12),activebackground="#111",activeforeground="crimson")
weak_radio.grid(row=2,column=1)
medium_radio.grid(row=2,column=2)
strong_radio.grid(row=2,column=3)
submit_button = Button(input_frame,text="Get Password",bd=0,bg="lightblue",height=2,width=20,font=font.Font(family="Helvetica",size=12),command=output)
submit_button.grid(row=3,column=1)
master.mainloop()
