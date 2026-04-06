from tkinter import *

root = Tk()
root.geometry('300x200')
root.title("Simple GUI Application in Python")
root.configure(bg="light grey")

def say_hi ():
   Label(root, text="Hi, Welcome to GUI in Python", font=("Arial",15), background="light grey", foreground="black").place(x=20,y=70)

clickBnt = Button(root, text="Click Me", background="light grey", activebackground="green", foreground="black", activeforeground="white", font=("Verdana",12), command=say_hi).place(x=50,y=130)
quitBtn = Button(root, text="Quit", background="light grey", activebackground="green", foreground="white", activeforeground="white", font=("Verdana",12), command=root.destroy).place(x=200,y=130)

root.mainloop()