#main window
'''from tkinter import *
top = Tk()
top.mainloop()''' 

#pack geometry
'''from tkinter import * 
top=Tk() 
button1=Button(top,fg='red',text='Red Button')
button1.pack(side=LEFT)
button2=Button(top,fg='blue',text='Blue Button')
button2.pack(side=RIGHT)
button3=Button(top,fg='green',text='Green Button')
button3.pack(side=TOP)
button4=Button(top,fg='yellow',text='Yellow Button')
button4.pack(side=BOTTOM)
top.mainloop()''' 

#grid geometry 
'''from tkinter import * 
top=Tk() 
name=Label(top,text="name").grid(row=0,column=0)
e1=Entry(top).grid(row=0,column=1)
password=Label(top,text="password").grid(row=1,column=0)
e2=Entry(top).grid(row=1,column=1)
top.mainloop()''' 

#place geometry 
'''from tkinter import * 
top=Tk() 
top.geometry("400x400")
l1=Label(top,text="name").place(x=0,y=10)
l2=Label(top,text="password").place(x=0,y=40)
e1=Entry(top).place(x=30,y=10)
e2=Entry(top).place(x=30,y=40)
btn1=Button(top,text='submit',activebackground="blue",activeforeground='magenta').place(x=0,y=80)
top.mainloop()''' 

#calculator 
'''import tkinter as tk
from tkinter import messagebox,Text
top = tk.Tk()
top.title("Addition Calculator")
# Function to perform addition
def add():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        display_text.delete("1.0", tk.END) # Clear existing text in the Text widget
        result = num1 + num2
        display_text.insert(tk.END, f"result: {result}\n")
        messagebox.showinfo("Result", f"The sum is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
# Create labels and entry fields for numbers
label_num1 = tk.Label(top, text="Number 1:")
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(top)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(top, text="Number 2:")
label_num2.grid(row=1, column=0)
entry_num2 = tk.Entry(top)
entry_num2.grid(row=1, column=1)
# Create a button for addition
button_add = tk.Button(top, text="Add", command=add)
button_add.grid(row=2, column=0, columnspan=2)
display_text=Text(top,height=3,width=30)
display_text.grid(row=5,column=4)
top.mainloop()'''


#listbox 
'''from tkinter import * 
top=Tk() 
top.geometry("800x500")
l1=Label(top,text="list of countries")
lb=Listbox(top)
lb.insert(1,'India')
lb.insert(2,"USA")
lb.insert(3,"Japan")
l1.pack() 
lb.pack()
top.mainloop()''' 

#checkbox 
'''from tkinter import * 
top=Tk() 
top.geometry("800x500")
mb=Menubutton(top,text="Language",relief=FLAT)
mb.grid() 
mb.menu=Menu(mb)
mb["menu"]=mb.menu
mb.menu.add_checkbutton(label='Hindi',variable=IntVar())
mb.menu.add_checkbutton(label='English',variable=IntVar())
mb.pack() 
top.mainloop()''' 

#menu 
'''from tkinter import * 
top=Tk() 
mb=Menu(top)
file=Menu(mb,tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="SaveAs")
file.add_separator() 
file.add_command(label="Exit",command=top.quit)
mb.add_cascade(label='file',menu=file)
edit=Menu(mb,tearoff=0)
edit.add_command(label="cut")
edit.add_command(label="copy")
edit.add_command(label="paste")
edit.add_command(label="select all")
mb.add_cascade(label="Edit",menu=edit)
help=Menu(mb,tearoff=0)
help.add_command(label="about")
mb.add_cascade(label="Help",menu=help)
top.config(menu=mb)
top.mainloop()'''

#change font of label 
'''from tkinter import * 
top=Tk() 
top.geometry("800x500")
l1=Label(top,text="label1",font=("arial bold",70)).grid(row=0,column=0)
top.resizable(0,0)
top.mainloop()'''

'''from tkinter import * 
top=Tk() 
top.geometry("800x500")
top.resizable(0,0)
top.title("button and button2")
b1=Button(text="Button1",font=('arial bold',10),command=None,activeforeground='red',activebackground='blue',width=30,height=50).grid(row=0,column=0)
b2=Button(text="Button2",font=('arial bold',10),command=None,activeforeground='red',activebackground='blue',width=30,height=50).grid(row=0,column=1)
top.mainloop()'''

#create a text widget and delete last two characters
'''import tkinter as tk
parent = tk.Tk()
mytext = tk.Text(parent)
mytext.insert('1.0', "- Python exercises, solution -")
mytext.insert('1.19', ' Practice,')
mytext.delete('1.0')
mytext.delete('end - 2 chars')
mytext.pack()
parent.mainloop()'''

#progress bar 
'''import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk
parent = tk.Tk()
parent.title("Progressbar")
parent.geometry('350x200')
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='green')
bar = Progressbar(parent, length=220, style='black.Horizontal.TProgressbar')
bar['value'] = 80
bar.grid(column=0, row=0)
parent.mainloop()'''

#radio button
'''import tkinter as tk
parent = tk.Tk()
parent.title("Radiobutton ")
parent.geometry('350x200')
radio1 = tk.Radiobutton(parent, text='First', value=1)
radio2 = tk.Radiobutton(parent, text='Second', value=2)
radio3 = tk.Radiobutton(parent, text='Third', value=3)
radio1.grid(column=0, row=0)
radio2.grid(column=1, row=0)
radio3.grid(column=2,row=0)
parent.mainloop()'''

#spinbox 
'''import tkinter as tk
top= tk.Tk()
text_var=tk.DoubleVar() 
spinbox = tk.Spinbox(top,from_=0.6,to=50.0,increment=0.1,textvariable=text_var).grid(row=0,column=0)
top.mainloop()'''

#loginform 
'''import tkinter as tk 
from tkinter import Checkbutton, IntVar, messagebox,Label,Entry,Button,Text
top=tk.Tk() 
top.title("LoginForm")
top.geometry("800x500")
def login(): 
    username=entry_username.get() 
    password=entry_password.get() 
    display_text.delete("1.0", tk.END) # Clear existing text in the Text widget
    display_text.insert(tk.END, f"Username: {username}\nPassword: {password}\n")  # Insert username and password to the TextArea
    if username=="user" and password=="123": 
        messagebox.showinfo("login successful")
        if var.get() == 1:
            display_text.insert(tk.END, "Remember me: Yes")
        else:
            display_text.insert(tk.END, "Remember me: No")
    else:
        messagebox.showerror("invalid credentials")
def submit(): 
    login()
l1=Label(top,text="username").grid(row=0,column=0)
entry_username=Entry(top)
entry_username.grid(row=0,column=1)
l2=Label(top,text="password").grid(row=1,column=0)
entry_password=Entry(top,show="*")
entry_password.grid(row=1,column=1)
b1=Button(top,text="submit",command=submit,width=5,height=10).grid(row=2,column=0)
entry_submit=Label(top).grid(row=2,column=1)

var = IntVar()
checkbox = Checkbutton(top, text="Remember me", variable=var)
checkbox.grid(row=2, column=0)

display_text=Text(top,height=3,width=30)
display_text.grid(row=5,column=4)
top.mainloop()'''




