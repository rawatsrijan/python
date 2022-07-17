from tkinter import *
import pyttsx3
root = Tk()
root.title("srijan rawat mini project")
label=Label(root,text="MINI ProJect\n \n\nTEXT TO VOICE CONVERTER\n\n\n\n ",bg="white",fg="orange",width=112,height=9)
label.pack()
root.minsize(width=1000,height=5000)
root.maxsize(width=1000,height=8000)
l = Label(root,text="Enter the word here-->>",bg="pink",height=10)
l.place(x=0,y=590)
e = Entry(root, width=30)
e.place(x=180,y=658)
def srijan():
    a=pyttsx3.init()
    a.say(e.get())
    a.runAndWait()
b=Button(root,text="SPEAK",bg="red",fg="black",command=srijan)
b.place(x=270,y=700)

p= PhotoImage(file="/Users/srijanrawat/Desktop/r.png")
o = Label(root,image=p,width=788,height=410)
o.place(x=10,y=150)


root.mainloop()
