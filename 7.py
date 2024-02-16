#automaticaly close window
from tkinter import*
win=Tk()
win.geometry("750x270")
Label(win,text="this window ",
font=("Arial","20","bold")).pack(pady=20)
win.after(5000,lambda:win.destroy())
win.mainloop()
