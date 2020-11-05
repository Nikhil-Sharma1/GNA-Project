from tkinter import *
from tkinter import ttk
import tkinter

root = Tk()



notebook = ttk.Notebook(root)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)
frame5 = ttk.Frame(notebook)
frame6 = ttk.Frame(notebook)

notebook.add(frame1, text="Q1")
notebook.add(frame2, text="Q2")
notebook.add(frame3, text="Q3")  
notebook.add(frame4, text="Q4")  
notebook.add(frame5, text="Q5")  
notebook.add(frame6, text="Q6")   



def displayscore(total):
    score = Tk()
    score.geometry("760x450")
    score.title("Score")
    score.configure(background="#000138")
    Label(score, text="Your score is: ", fg="Black", font="Arial 36").pack()
    T = Text(score, height=2, width=30 )
    T.pack()
    T.tag_configure("center", justify='center')
    T.insert(tkinter.END,marks)
    T.tag_add("center", "1.0", "end")

global ques,marks
ques=0
marks=0
def flagset():
    global ques,marks
    ques=ques+1
    if ques == 6:
        displayscore(marks)
        

def totalset():
    global marks
    marks=marks+1


def main():
    def correct():
        list = frame1.grid_slaves()
        for l in list:
            l.destroy()
        Label(frame1, text="Correct").grid(row=1,column=5)
        flagset()
        totalset()


    def incorrect():
        list = frame1.grid_slaves()
        for l in list:
            l.destroy()
        Label(frame1, text="Incorrect").grid(row=2,column=5)
        flagset()



    
    #Question 1
    var = IntVar()
    Label(frame1, text="Where is the '7' in 1704?").grid(row=2,column=3)
    Button(frame1, text="In the Thousands", command=incorrect, width=15).grid(row=7, column=1)
    Button(frame1, text="In the Hundreds", command=correct, width=15).grid(row=7, column=3)
    Button(frame1, text="In the Tens", command=incorrect, width=15).grid(row=7, column=5)
    Button(frame1, text="In the Ones", command=incorrect, width=15).grid(row=7, column=7)
  




    def correct2():
        list = frame2.grid_slaves()
        for l in list:
            l.destroy()
        Label(frame2, text="Correct").grid(row=1,column=5)
        flagset()
        totalset()

    def incorrect2():
        list = frame2.grid_slaves()
        for l in list:
            l.destroy()
        Label(frame2, text="Incorrect").grid(row=1,column=5)
        flagset()

    #Question2
    Label(frame2, text="What is 1704 in words?").grid(row=2,column=3)
    Button(frame2, text="One Million, Seven thousand and Four", command=incorrect2, width=35).grid(row=5,column=1)
    Button(frame2, text="One Hundred and Seventy Four", command=incorrect2, width=35).grid(row=5, column=2)
    Button(frame2, text="One Thousand and Seventy Four", command=incorrect2, width=35).grid(row=5, column=3)
    Button(frame2, text="One Thousand, Seven Hundred and Four", command=correct2, width=35).grid(row=5, column=4)

    #Question 3

    def correct3():
        list = frame3.grid_slaves()
        for l in list:
            l.destroy()
        Label(frame3, text="Correct").grid(row=1,column=5)
        flagset()
        totalset()

    def incorrect3():
        list = frame3.grid_slaves()
        for l in list:
            l.destroy()
        Label(frame3, text="Incorrect").grid(row=1,column=5)
        flagset()


    Label(frame3, text="Find ?: 3 x ? = 18").grid(row=2,column=3)
    Button(frame3, text="6", command=correct3, width=20).grid(row=5, column=1)
    Button(frame3, text="7", command=incorrect3, width=20).grid(row=5, column=2)
    Button(frame3, text="8", command=incorrect3, width=20).grid(row=5, column=3)
    Button(frame3, text="9", command=incorrect3, width=20).grid(row=5, column=4)


    #Question 4


    def correct4():
        list = frame4.grid_slaves()
        for l in list:
            l.destroy()
        Label(frame4, text="Correct").grid(row=1,column=5)
        flagset()
        totalset()

    def incorrect4():
        list = frame4.grid_slaves()
        for l in list:
            l.destroy()
        Label(frame4, text="Incorrect").grid(row=1,column=5)
        flagset()

    Label(frame4, text="What is the moniter?").grid(row=2,column=3)
    Button(frame4, text="A display that shows what the computer is doing",command=correct4, width=40).grid(row=5,column=1)
    Button(frame4, text="A circut board", command=incorrect4, width=20).grid(row=5,column=2)
    Button(frame4, text="A Program", command=incorrect4, width=20).grid(row=5,column=3)
    Button(frame4, text="A window", command=incorrect4, width=20).grid(row=5,column=4)

    #Question 5


    def correct5():
        list = frame5.grid_slaves()
        for l in list:
            l.destroy()
        Label(frame5, text="Correct").grid(row=1,column=5)
        flagset()
        totalset()

    def incorrect5():
        list = frame5.grid_slaves()
        for l in list:
            l.destroy()
        Label(frame5, text="Incorrect").grid(row=1,column=5)
        flagset()


    Label(frame5, text="What does the 'from ____ import' command do?").grid(row=2,column=3)
    Button(frame5, text="Import an image",command=incorrect5, width=15).grid(row=5,column=1)
    Button(frame5, text="Import text", command=incorrect5, width=15).grid(row=5,column=2)
    Button(frame5, text="Import a module", command=correct5, width=15).grid(row=5,column=3)
    Button(frame5, text="Send a module", command=incorrect5, width=15).grid(row=5,column=4)


    #Question 6
    def correct6():
        list = frame6.grid_slaves()
        for l in list:
            l.destroy()
        Label(frame6, text="Correct").grid(row=1,column=5)
        totalset()
        flagset()

    def incorrect6():
        list = frame6.grid_slaves()
        for l in list:
            l.destroy()
        Label(frame6, text="Incorrect").grid(row=1,column=5)
        flagset()

    Label(frame6, text="Which of these is a Boolean Value?").grid(row=2,column=3)
    Button(frame6, text="Enter",command=incorrect6, width=15).grid(row=5,column=1)
    Button(frame6, text="Esc", command=incorrect6, width=15).grid(row=5,column=2)
    Button(frame6, text="True", command=correct6, width=15).grid(row=5,column=3)
    Button(frame6, text="False", command=incorrect6, width=15).grid(row=5,column=3)






main()

notebook.pack()

root.mainloop()