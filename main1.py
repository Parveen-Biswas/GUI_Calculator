from tkinter import *

root = Tk()
root.geometry("305x450+550+200")
root.title("Calculator")
window_icon = PhotoImage(file="icon/calculator.png")
root.iconphoto(False, window_icon)
root.resizable(False,False)
# root.configure(bg="black")
######################################################################################################################
text_input = StringVar()
operator = ""
######################################################################################################################
def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btncleardisplay():
    global operator
    operator = ""
    text_input.set("")

def btnequalinput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup) 
    operator = ""
######################################################################################################################
input_entry = Entry(root, width=19, textvariable=text_input, justify=RIGHT, font="Arial 20", border=2, relief=SOLID)
input_entry.place(x=7, y= 20, height=60)
######################################################################################################################
btnD = Button(root, text='.', command=lambda:btnclick("."), font="popins 15 bold", width= 5, height=2, border=2, relief=SOLID)
btnD.place(x=5, y=365)
btn0 = Button(root, text='0', font="popins 15 bold", width= 5, height=2, border=2, relief=SOLID, command=lambda:btnclick(0))
btn0.place(x=80, y=365)
btnE = Button(root, text='=', font="popins 15 bold", width= 5, height=2, border=2, relief=SOLID, command=btnequalinput)
btnE.place(x=155, y=365)
btnA = Button(root, text='+', font="popins 15 bold", width= 5, height=2, border=2, relief=SOLID, command=lambda:btnclick("+"))
btnA.place(x=230, y=365)
######################################################################################################################
btn1 = Button(root, text='1', font="popins 15 bold", width= 5, height=2, border=2, relief=SOLID, command=lambda:btnclick(1))
btn1.place(x=5, y=295)
btn2 = Button(root, text='2', font="popins 15 bold", width= 5, height=2, border=2, relief=SOLID, command=lambda:btnclick(2))
btn2.place(x=80, y=295)
btn3 = Button(root, text='3', font="popins 15 bold", width= 5, height=2, border=2, relief=SOLID, command=lambda:btnclick(3))
btn3.place(x=155, y=295)
btnS = Button(root, text='-', font="popins 15 bold", width= 5, height=2, border=2, relief=SOLID, command=lambda:btnclick("-"))
btnS.place(x=230, y=295)
######################################################################################################################
btn4 = Button(root, text='4', font="popins 15 bold", width= 5, height=2, border=2, relief=SOLID, command=lambda:btnclick(4))
btn4.place(x=5, y=225)
btn5 = Button(root, text='5', font="popins 15 bold", width= 5, height=2, border=2, relief=SOLID, command=lambda:btnclick(5))
btn5.place(x=80, y=225)
btn6 = Button(root, text='6', font="popins 15 bold", width= 5, height=2, border=2, relief=SOLID, command=lambda:btnclick(6))
btn6.place(x=155, y=225)
btnM = Button(root, text='x', font="popins 15 bold", width= 5, height=2, border=2, relief=SOLID, command=lambda:btnclick("*"))
btnM.place(x=230, y=225)
######################################################################################################################
btn7 = Button(root, text='7', font="popins 15 bold", width= 5, height=2, border=2, relief=SOLID, command=lambda:btnclick(7))
btn7.place(x=5, y=155)
btn8 = Button(root, text='8', font="popins 15 bold", width= 5, height=2, border=2, relief=SOLID, command=lambda:btnclick(8))
btn8.place(x=80, y=155)
btn9 = Button(root, text='9', font="popins 15 bold", width= 5, height=2, border=2, relief=SOLID, command=lambda:btnclick(9))
btn9.place(x=155, y=155)
btnDIV = Button(root, text='/', font="popins 15 bold", width= 5, height=2, border=2, relief=SOLID, command=lambda:btnclick("/"))
btnDIV.place(x=230, y=155)
btnC = Button(root, text='C', font="popins 15 bold", width= 23, height=2, border=2, relief=SOLID, command=btncleardisplay)
btnC.place(x=9, y=85)
######################################################################################################################

root.mainloop()