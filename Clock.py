# from tkinter import *
# from tkinter.ttk import *
# from time import  strftime
#
# root =Tk()
# root.title("Clock")
#
# def time():
#     string =strftime("%H:%M:%S:%p")
#     label.config(text=string)
#     label.after(1000,time)
#
# label = Label(root,font=("ds-digital",80),background="black",foreground="yellow")
# label.pack(anchor="center")
# time()
# mainloop()


from tkinter import *
from tkinter.ttk import *
from time import strftime

def time():
    string = strftime("%H:%M:%S:%p")
    label.config(text=string)
    label.after(1000,time)

root =Tk()
root.title("Clock Time")


label = Label (root,font=("ds-digit",80),background="black",foreground="yellow")
label.pack(anchor="center")
time()
mainloop()




