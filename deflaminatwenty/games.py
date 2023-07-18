from tkinter import *
from dictionary import *

import os, sys
from tkinter.messagebox import showinfo
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
pathcanvas =  os.path.join(dirname, "zoo3.png")
pathquit = os.path.join(dirname, "quit.png")
pathtrue = os.path.join(dirname, "true.png")
pathfalse = os.path.join(dirname, "false.png")


qnum = 0
score = 0
def gameplay():
    root = Tk()
    root.title("Animal Game")
    root.eval('tk::PlaceWindow . center')

    running = Label(text="game is running")
    running.pack()


    def createquestion():
        def clickedTrue():
            answer = 'True'
            window1.withdraw()
            check_answer(answer)
        
        def clickedFalse():
            answer = 'False'
            window1.withdraw()
            check_answer(answer)

        def clickedHint():
            def hintclose():
                hintwindow.destroy()
                window1.deiconify()
            window1.withdraw()

            hintwindow = Tk()
            hintwindow.title("Only 1 hint!")
            hint = Label(hintwindow,text=hint_dict[qnum],font=("Times New Roman", 20),background="white",foreground="black",width=100,height = 10)
            hint.pack()
            okhint = Button(hintwindow,text='Got it',command=hintclose)
            okhint.pack()

        def closewindow(windo):
            windo.destroy()
            window1.destroy()
            createquestion()
            
        def check_answer(answer):
            global score
            answerwindow = Tk()
            answerwindow.attributes('-fullscreen',True)
            dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
            pathcanvas =  os.path.join(dirname, "zoo3.png")
            answnd=Canvas(answerwindow,bg="black",height=100,width=100)
            filename=PhotoImage(master=answerwindow,file=str(pathcanvas))
            background_label = Label(answerwindow,image=filename)
            background_label.place(x=0,y=0, relwidth=1,relheight=1)
            answerwindow.title("Animal Game")
            answerwindow.eval('tk::PlaceWindow . center')
            if answer == answer_dict[qnum]:
                yayornay = "Correct!"
                score += 1
            elif answer != answer_dict[qnum]:
                yayornay = "Incorrect!"+ '\n' + ifwrong_dict[qnum]

            
            correctorno = Label(answerwindow,text=yayornay,font=("Times New Roman", 35),background="white",foreground="black")
            correctorno.pack(pady=300)
            closeanswer = Button(answerwindow,text="OK",font=("Times New Roman", 25),command=lambda:closewindow(answerwindow))
            closeanswer.pack()
            answnd.pack()
            answerwindow.mainloop()

        def resultpage():
            def quit_clicked():
                showinfo(
                title='Quit',
                message='Game Quit - See you next time!'
                )
                resultpaged.destroy()

            resultpaged = Tk()
            dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
            pathcanvas =  os.path.join(dirname, "zoo3.png")
            resultbg=Canvas(resultpaged,bg="black",height=100,width=100)
            filename=PhotoImage(master=resultpaged,file=str(pathcanvas))
            background_label = Label(resultpaged,image=filename)
            background_label.place(x=0,y=0, relwidth=1,relheight=1)

            resultpaged.attributes('-fullscreen',True)
            scoremessage = 'Congratulations! Your score is'+' '+str(score)
            display_result = Label(resultpaged,text=scoremessage,font=("Times New Roman", 40),background="black",foreground="white")
            display_result.pack(pady=350)
            
            quit = PhotoImage(file=str(pathquit))
            getoutofgame = Button(resultpaged,text="Quit",font=("Times New Roman", 40),background="white",foreground="red", command=quit_clicked)
            
            getoutofgame.pack()
            resultbg.pack()
            
            resultpaged.mainloop()

        window1 = Toplevel() #toplevel to run new window on top of main window
        window1.title("def LaminaTwenty()")
        window1.attributes('-fullscreen',True)
        c=Canvas(window1,bg="black",height=100,width=100)

        filename=PhotoImage(file=str(pathcanvas))
        background_label = Label(window1,image=filename)
        background_label.place(x=0,y=0, relwidth=1,relheight=1)

        root.withdraw() #temporarily hides ugly main window
        
        global qnum
        qnum +=1
        if qnum > len(question_dict):
            global score
            print(score)
            window1.destroy()
            resultpage()
            
        qnumtext = 'Question',qnum
        qnumlabel = Label(window1,text=qnumtext,font=("Times New Roman", 30),background="white",foreground="black")
        qnumlabel.pack(pady=105)

        questionlabel = Label(window1,text=question_dict[qnum],font=("Times New Roman", 35),background="white",foreground="black")
        questionlabel.pack(pady=20)

        true = PhotoImage(file=str(pathtrue))
        false = PhotoImage(file=str(pathfalse))

        hintbutton = Button(window1,text="Need help?",font=("Times New Roman", 15),command=clickedHint)
        hintbutton.pack()
        truebutton = Button(window1,image=true,command=clickedTrue)
        truebutton.pack(side = 'left',padx=335)
        falsebutton = Button(window1,image=false,command=clickedFalse)
        falsebutton.pack(side = 'right',padx=330)

        
        
        c.pack() #packing canvas
        window1.mainloop()
    createquestion()
    root.mainloop()