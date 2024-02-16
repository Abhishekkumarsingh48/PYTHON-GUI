from tkinter import *
win=Tk()
win.geometry("750x450+300+200")
#win.attributes('-fullscreen',True)
win.title("Abhishek")
mylabel1=Label(win,text="user name",foreground="white",background="dodgerblue",font=("Algerian","20","bold"))
mylabel2=Label(win,text="password",foreground="white",background="dodgerblue",font=("Algerial","20","bold"))
#mylabel1.grid(row=0,column=0)
#mylabel2.grid(row=1,column=1)
mylabel1.pack(pady=10)
mylabel2.pack(pady=10)
counter=0
def click():
    global counter
    global lbl3
    counter=counter+1
    lbl3.configure(text=f'you clicked{counter}times')
    if counter>5:
        mybutton.configure(state=DISABLED)
        lbl3.configure(text="try after sometimes")
lbl3=Label(win,text="successfuly Registered")
lbl3.pack()
mybutton=Button(win,text="submit",bg="blue",command=click)
mybutton.pack(pady=10)
canvas=Canvas(win,bg='dodgerblue')
'''canvas.pack(expand=True)
canvas.create_rectangle(40,20,50,60)
canvas.create_line(30,20,40,60)
canvas.create_rectangle(60,40,100,120)
canvas.create_oval(100,150,200,250)'''
win.mainloop()
