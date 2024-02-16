from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Abhishek")
root.geometry("350x225+350+350")
lbl=Label(root,text="user name")
lbl.pack()
ent=Entry(root,width=30)
ent.pack()
ent.insert(0,"Enter user name")
def click():
    x=ent.get()
    lbl1=Label(root,text="Mr  "+x)
    lbl1.pack()
    ent.delete(0,END)
lbl2=Label(root,text="password")
lbl2.pack()
ent1=Entry(root,width=30)
ent1.pack()
ent1.insert(0,"Enter password")
def display():
    messagebox.showinfo("title","you have succefully Registered?")
    root.destroy #for closing window after submit
btn=Button(root,text="submit",bg="lightblue",command=display)
btn.pack()
'''def view():
    messagebox.showinfo("title","realy want to cancle")'''
btn1=Button(root,text="cancle",bg="red")
btn.pack()
root.mainloop()
