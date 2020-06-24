import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
win = tk.Tk()
win.resizable(0,0)
win.title('Calculator')

val = ""
A = 0
oper = ""
count = 0
count1 = 0

def btn2_clicked():
    global val
    if "." in val:
        text_var.set(0) 
    elif val == '':
        text_var.set(val)
        pass
    else:
        val = list(val)
        l = ""
        del val[-1]
        val = l.join(val)
        text_var.set(val)

def btn17_clicked():
    global val
    global A
    val2 = val
    if oper == "+":
        x = float((val2.split("+")[1]))
        c1 = x**-1
        c1 = A + c1
        text_var.set(c1)
    elif oper == "-":
        x = float((val2.split("-")[1]))
        c1 = x**-1
        c1 = A - c1
        text_var.set(c1)
    elif oper == "*":
        x = float((val2.split("*")[1]))
        c1 = x**-1
        c1 = A * c1
        text_var.set(c1)
    elif oper == "/":
        x = float((val2.split("/")[1]))
        c1 = x**-1
        c1 = A / c1
        text_var.set(c1)
    else:
        if "." in val :
            val = float(val)
        else:
            val = int(val)
        val = val**-1
        text_var.set(val)

def btn3_clicked():
    global val
    global A
    val2 = val
    if val[-1]=='+' or val[-1]=='-' or val[-1]=='*' or val[-1]=='/' :
        val = list(val)
        l = ""
        del val[-1]
        val = l.join(val)
        val = int(val)
        val = val/100
        text_var.set(val)
    elif oper == "+":
        x = float((val2.split("+")[1]))
        c1 = A*x/100
        c1 = c1 + A
        text_var.set(c1)
    elif oper == "-":
        x = float((val2.split("-")[1]))
        c1 = A*x/100
        c1 = A - c1
        text_var.set(c1)
    elif oper == "*":
        x = float((val2.split("*")[1]))
        c1 = A*x/100
        text_var.set(c1)
    elif oper == "/":
        x = float((val2.split("/")[1]))
        c1 = x/100
        c1 = A/c1
        text_var.set(c1)
    else:
        if "." in val :
            val = float(val)
        else:
            val = int(val)
        val = val/100
        text_var.set(val)

def btn20_clicked():
    global val
    global A
    global oper
    val2 = val
    if val[-1]=='+' or val[-1]=='-' or val[-1]=='*' or val[-1]=='/' :
        # messagebox.showerror("Error","Please enter valid Expression")
        if val == '':
            pass
        else:
            val = list(val)
            l = ""
            del val[-1]
            val = l.join(val)
            text_var.set(val)
    elif oper == "+":
        x = float((val2.split("+")[1]))
        c = A + x
        val = str(c)
        if '.' in val:
            if val[-1]=='0':
                c1 = int(c)
                val = list(val)
                l = ''
                del val[-1]
                del val[-1]
                val = l.join(val)
            else :
                c1 = float(c)
        text_var.set(c1)
        oper = ""
    elif oper == '-':
        x = float((val2.split("-")[1]))
        c = A - x
        val = str(c)
        if '.' in val:
            if val[-1]=='0':
                c1 = int(c)
                val = list(val)
                l = ''
                del val[-1]
                del val[-1]
                val = l.join(val)
            else :
                c1 = float(c)
        text_var.set(c1)
        oper = ''
    elif oper == '*':
        x = float((val2.split("*")[1]))
        c = A * x
        val = str(c)
        if '.' in val:
            if val[-1]=='0':
                c1 = int(c)
                val = list(val)
                l = ''
                del val[-1]
                del val[-1]
                val = l.join(val)
            else :
                c1 = float(c)
        text_var.set(c1)
        oper = ''
    elif oper == '/':
        x = float((val2.split("/")[1]))
        if x==0:
            messagebox.showerror("Error","Division by Zero Not Allowed")
            A = 0
            val = ""
            oper = ""
            text_var.set(val)
        else:
            c = A / x
            val = str(c)
            if '.' in val:
                if val[-1]=='0':
                    c1 = int(c)
                    val = list(val)
                    l = ''
                    del val[-1]
                    del val[-1]
                    val = l.join(val)
                else :
                    c1 = float(c)
            text_var.set(c1)
            oper = ""
    else :
        if '.' in val2:
            val2 = float(val)
        else :
            val2 = int(val)
        text_var.set(val2)

def btn1_clicked():
    global val
    global oper
    global A
    A = 0
    oper = ""
    val = ""
    text_var.set(val)


def btn4_clicked():
    global val
    global oper
    global A
    global count1
    global count
    if count1 == count + 1:
        btn20_clicked()
    if val[-1]=='+' or val[-1]=='-' or val[-1]=='*' or val[-1]=='/' :
        val = list(val)
        l = ''
        del val[-1]
        val = l.join(val)
        val + val + '/'
    else:
        A = float(val)
        oper = "/"
        val = val + oper
    text_var.set(val)
    count1 = count + 1

def btn8_clicked():
    global val
    global oper
    global A
    global count1
    global count
    if count1 == count + 1:
        btn20_clicked()
    if val[-1]=='+' or val[-1]=='-' or val[-1]=='*' or val[-1]=='/' :
        val = list(val)
        l = ''
        del val[-1]
        val = l.join(val)
        val = val + '*'
    else:
        A = float(val)
        oper = "*"
        val = val + oper
    text_var.set(val)
    count1 = count + 1

def btn12_clicked():
    global val
    global oper
    global A
    global count1
    global count
    if count1 == count + 1:
        btn20_clicked()
    if val == '':
        val = val + '-'
    elif val[-1]=='+' or val[-1]=='-' or val[-1]=='*' or val[-1]=='/' :
        val = list(val)
        l = ''
        del val[-1]
        val = l.join(val)
        val = val + '-'
    else:
        A = float(val)
        oper = "-"
        val = val + oper
    text_var.set(val)
    count1 = count + 1

def btn16_clicked():
    global val
    global oper
    global A
    global count1
    global count
    if count1 == count + 1:
        btn20_clicked()
    if val == '':
        val = val + '+'
    elif val[-1]=='-' or val[-1]=='*' or val[-1]=='/' or val[-1]=='+' :
        val = list(val)
        l = ''
        del val[-1]
        val = l.join(val)
        val = val + '+'
    else:
        A = float(val)
        oper = "+"
        val = val + oper
    text_var.set(val)
    count1 = count + 1

def btn5_clicked():
    global val
    val = val + "1"
    text_var.set(val)

def btn19_clicked():
    global val
    val = val + "."
    text_var.set(val)

def btn6_clicked():
    global val
    val = val + "2"
    text_var.set(val)

def btn7_clicked():
    global val
    val = val + "3"
    text_var.set(val)

def btn9_clicked():
    global val
    val = val + "4"
    text_var.set(val)

def btn10_clicked():
    global val
    val = val + "5"
    text_var.set(val)

def btn11_clicked():
    global val
    val = val + "6"
    text_var.set(val)

def btn13_clicked():
    global val
    val = val + "7"
    text_var.set(val)

def btn14_clicked():
    global val
    val = val + "8"
    text_var.set(val)

def btn15_clicked():
    global val
    val = val + "9"
    text_var.set(val)

def btn18_clicked():
    global val
    val = val + "0"
    text_var.set(val)

text_var = tk.StringVar()
text_var.set(0)
textdisplay = tk.Label(win, bd = 20, height = 2, textvariable = text_var, anchor = "se", font = ('Verdana',20), background = '#ffffff',fg = '#000000')
textdisplay.pack(expand = True, fill = 'both')

topframe = tk.Frame(win)
topframe.pack(expand = True, fill = 'both')

b1 = tk.Button(topframe, padx = 20, pady = 20, text = 'AC', border = 0, fg = 'black', font = ('Verdana',18), command = btn1_clicked)
b1.pack(side = 'left',expand = 'True', fill = 'both')


b2 = tk.Button(topframe, padx = 20, pady = 20, text = 'C', border = 0, fg = 'black', font = ('Verdana',18), command = btn2_clicked)
b2.pack(side = 'left',expand = 'True', fill = 'both')

b3 = tk.Button(topframe, padx = 20, pady = 20, text = '%', border = 0, fg = 'black',font = ('Verdana',22), command = btn3_clicked)
b3.pack(side = 'left',expand = 'True', fill = 'both')

b4 = tk.Button(topframe, padx = 20, pady = 20, text = '/', border = 0, fg = 'black', font = ('Verdana',22), command = btn4_clicked)
b4.pack(side = 'left',expand = 'True', fill = 'both')

frame1 = tk.Frame(win)
frame1.pack(expand = 'True', fill = 'both')

b5 = tk.Button(frame1, padx = 20, pady = 20, text = '1', border = 0, fg = 'black',command = btn5_clicked, font = ('Verdana',22))
b5.pack(side = 'left',expand = 'True', fill = 'both')

b6 = tk.Button(frame1, padx = 20, pady = 20, text = '2', border = 0, fg = 'black',command = btn6_clicked, font = ('Verdana',22))
b6.pack(side = 'left',expand = 'True', fill = 'both')

b7 = tk.Button(frame1, padx = 20, pady = 20, text = '3', border = 0, fg = 'black',command = btn7_clicked, font = ('Verdana',22))
b7.pack(side = 'left',expand = 'True', fill = 'both')

b8 = tk.Button(frame1, padx = 20, pady = 20, text = '*', border = 0, fg = 'black', font = ('Verdana',22), command = btn8_clicked)
b8.pack(side = 'left',expand = 'True', fill = 'both')

frame2 = tk.Frame(win)
frame2.pack(expand = 'True', fill = 'both')

b9 = tk.Button(frame2, padx = 20, pady = 20, text = '4', border = 0, fg = 'black',command = btn9_clicked, font = ('Verdana',22))
b9.pack(side = 'left',expand = 'True', fill = 'both')

b10 = tk.Button(frame2, padx = 20, pady = 20, text = '5', border = 0, fg = 'black',command = btn10_clicked, font = ('Verdana',22))
b10.pack(side = 'left',expand = 'True', fill = 'both')

b11 = tk.Button(frame2, padx = 20, pady = 20, text = '6', border = 0, fg = 'black',command = btn11_clicked, font = ('Verdana',22))
b11.pack(side = 'left',expand = 'True', fill = 'both')

b12 = tk.Button(frame2, padx = 20, pady = 20, text = '-', border = 0, fg = 'black', font = ('Verdana',22), command = btn12_clicked)
b12.pack(side = 'left',expand = 'True', fill = 'both')

frame3 = tk.Frame(win)
frame3.pack(expand = 'True', fill = 'both')

b13 = tk.Button(frame3, padx = 20, pady = 20, text = '7', border = 0, fg = 'black',command = btn13_clicked, font = ('Verdana',22))
b13.pack(side = 'left',expand = 'True', fill = 'both')

b14 = tk.Button(frame3, padx = 20, pady = 20, text = '8', border = 0, fg = 'black',command = btn14_clicked, font = ('Verdana',22))
b14.pack(side = 'left',expand = 'True', fill = 'both')

b15 = tk.Button(frame3, padx = 20, pady = 20, text = '9', border = 0, fg = 'black',command = btn15_clicked, font = ('Verdana',22))
b15.pack(side = 'left',expand = 'True', fill = 'both')

b16 = tk.Button(frame3, padx = 20, pady = 20, text = '+', border = 0, fg = 'black', font = ('Verdana',22), command = btn16_clicked)
b16.pack(side = 'left',expand = 'True', fill = 'both')

frame4 = tk.Frame(win)
frame4.pack(expand = 'True', fill = 'both')

b17 = tk.Button(frame4, padx = 20, pady = 20, text = '1/x', border = 0, fg = 'black', font = ('Verdana',18), command = btn17_clicked)
b17.pack(side = 'left',expand = 'True', fill = 'both')

b18 = tk.Button(frame4, padx = 20, pady = 20, text = '0', border = 0, fg = 'black', command = btn18_clicked, font = ('Verdana',22))
b18.pack(side = 'left',expand = 'True', fill = 'both')

b19 = tk.Button(frame4, padx = 20, pady = 20, text = '.', border = 0, fg = 'black', font = ('Verdana',22), command = btn19_clicked)
b19.pack(side = 'left',expand = 'True', fill = 'both')

b20 = tk.Button(frame4, padx = 20, pady = 20, text = '=', border = 0, fg = 'black', font = ('Verdana',22), command = btn20_clicked)
b20.pack(side = 'left',expand = 'True', fill = 'both')

win.mainloop()