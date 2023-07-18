from tkinter import *
from tkinter import messagebox
from cc import charcreation
from tkinter.messagebox import showinfo
import os, sys
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
path =  os.path.join(dirname, "zoo3.png")
pathlogo = os.path.join(dirname, "logo.png")
pathquit = os.path.join(dirname, "quit.png")
pathplay = os.path.join(dirname, "play.png")

def mm():
    top = Tk()
    top.title("def LaminaTwenty() - Main Menu")
    #top.geometry("700x700+350+50")
    top.attributes('-fullscreen',True)
    c=Canvas(top,bg="black",height=100,width=100)
    filename=PhotoImage(file=str(path))
    background_label = Label(top,image=filename)
    background_label.place(x=0,y=0, relwidth=1,relheight=1)


    logo = PhotoImage(file=str(pathlogo))

    logolabel = Label(top, image=logo)
    logolabel.pack(pady = 200)


    def onPlay():
        
        top.withdraw()
        charcreation()

    play = PhotoImage(file=str(pathplay))
    b = Button( top, image=play,command=onPlay)
    b.pack()


    def onQuit():
        showinfo(
            title='Quit',
            message='Game Quit - See you next time!'
        )
        top.destroy()

    quit = PhotoImage(file=str(pathquit))
    
    quit_button = Button( 
        top, 
        image=quit, 
        compound=LEFT, 
        command=onQuit 
    ) 
    
    quit_button.pack( 
        ipadx=0.8, 
        ipady=0.8, 
        expand=True, 
    )


    c.pack()

    top.mainloop()