from tkinter import * 
from functools import partial 
top=Tk()
def call_result(label_result,n1,n2): 
    num1=(n1.get())
    num2=(n2.get())
    result=int(num1)+int(num2)
    label_result.config(test="Result:%d"%result)
    return 
number1=Tk.StringVar() 
number2=Tk.StringVar()
top.geometry("800x500")
top.title("calculator")
l1=Label(top,text="num1").grid(row=0,column=0)
l2=Label(top,text="num2").grid(row=1,column=0)
labelres=Label(top,text='Result').grid(row=3,column=0)
e1=Entry(top).place(row=1,column=1)
e2=Entry(top).place(row=1,column=1)
btn1=Button(top,text='calculate',activebackground="blue",activeforeground='magenta',command=call_result).grid(row=3,column=0)
call_result=partial(call_result,labelres,number1,number2)