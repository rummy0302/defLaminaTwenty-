from tkinter import *
from dictionary import *
from games import gameplay
from tkinter.messagebox import showinfo
import os, sys
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
path =  os.path.join(dirname, "zoo3.png")
pathtrue = os.path.join(dirname, "true.png")
pathfalse = os.path.join(dirname, "false.png")

name1 = "john"
def charcreation():
    def getentry():
        global name1
        name1=enter1.get()
        cc.destroy()
        showinfo(title="Welcome,", message=f"Welcome {name1}")
        print("Welcome, {}".format(name1))
        gameplay()
        return
        
    
    cc = Toplevel()
    cc.title("def LaminaTwenty - Welcome Page")
    #cc.geometry("700x700+350+50")
    cc.attributes('-fullscreen',True)
    c=Canvas(cc,bg="black",height=100,width=100)
    filename=PhotoImage(file=str(path))
    background_label = Label(cc,image=filename)
    background_label.place(x=0,y=0, relwidth=1,relheight=1)

    label = Label(cc, text = "Please enter name",
                font=("Times New Roman", 40),background="black",foreground="white",width=15,height=1)
    label.pack(pady = 150)

    label1 = Label(cc,text="Name",font=("Times New Roman", 20),background="white",foreground="black",width=15,height=1)
    label1.pack()

    enter1=Entry(cc,width=40)
    enter1.pack()

    submit_button=Button(cc,text="Submit",font=("Times New Roman", 20),background="white",foreground="blue",width=15,height=1,command=getentry)
    submit_button.pack()

    c.pack()
    cc.mainloop()
    return