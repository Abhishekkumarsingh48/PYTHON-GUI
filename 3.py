from tkinter import *
root=Tk()
root.title("Abhishek")
root.geometry("350x225+350+350")
#root.attributes('-fullscreen',True)
mylabel=Label(root,text="hello students",
foreground="white",background="dodgerblue")
mylabel2=Label(root,text="i am here",foreground="white",background="dodgerblue")
mylabel.pack(pady=50)
mylabel2.pack(pady=70)
root.mainloop()
