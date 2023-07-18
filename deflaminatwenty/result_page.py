from tkinter import * 
from mainmenu import *
#from games import score
from tkinter.messagebox import showinfo
import os, sys
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
path =  os.path.join(dirname, "quit.png")
#character_creation is title of weimings module which i dont have yet

#result2 = name2[score2]
#get results 
#print results 
def result_page():
    #global name1
    #global score
    resultpage = Tk()
    #window dimensions 
    #resultpage.geometry('700x700+350+50')
    resultpage.attributes('-fullscreen',True)
    display_result = Label(text= f"Congratulations{name}! Your score is {givescore}")
    display_result.pack()

    # Create a Button
    def go_main_menu():
        resultpage.destroy()
        mm()

    btn_menu = Button(resultpage, text='Go back to main menu', bd='5', command=go_main_menu)
                

    def quit_clicked():
        showinfo(
            title='Quit',
            message='Game Quit - See you next time!'
        )
        resultpage.destroy()


    quit_icon = PhotoImage(file=str(path))

    quit_button = Button(resultpage,
        image=quit_icon,
        text='Quit',
        compound=LEFT,
        command=quit_clicked
    )

    quit_button.pack(
        ipadx=5,
        ipady=5,
        expand=True,
        side=BOTTOM
    )


    # Set the position of button on the top of window.  
    #btn_quit.pack(side = 'RIGHT')  
    btn_menu.pack(side =LEFT) 

    resultpage.mainloop()

