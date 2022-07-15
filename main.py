from tkinter import *
import pyttsx3
root = Tk()
root.title("srijan rawat mini project")
label=Label(root,text="MINI ProJect\n TEXT TO VOICE CONVERTER ")
label.pack()
root.minsize(width=1000,height=5000)
root.maxsize(width=1000,height=8000)
l = Label(root,text="Enter the word here-->>",bg="pink")
l.place(x=0,y=40)
e = Entry(root, width=20)
e.place(x=160,y=40)
def srijan():
    a=pyttsx3.init()
    a.say(e.get())
    a.runAndWait()
b=Button(root,text="enter",bg="red",fg="red",command=srijan)
b.place(x=210,y=70)

p= PhotoImage(file="/Users/srijanrawat/Desktop/r.png")
o = Label(root,image=p,width=788,height=410)
o.place(x=10,y=200)


root.mainloop()