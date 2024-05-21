from tkinter import *

root = Tk()
root.geometry("305x450+550+200")
root.title("Calculator")
window_icon = PhotoImage(file="icon/calculator.png")
root.iconphoto(False, window_icon)
root.resizable(False,False)
root.configure(bg="black")

#image
zero = PhotoImage(file="icon/zero.png")
one = PhotoImage(file="icon/one.png")
two = PhotoImage(file="icon/two.png")
three = PhotoImage(file="icon/three.png")
four = PhotoImage(file="icon/four.png")
five = PhotoImage(file="icon/five.png")
six = PhotoImage(file="icon/six.png")
seven = PhotoImage(file="icon/seven.png")
eight = PhotoImage(file="icon/eight.png")
nine = PhotoImage(file="icon/nine.png")
add = PhotoImage(file="icon/add.png")
minus = PhotoImage(file="icon/minus.png")
asterisk = PhotoImage(file="icon/asterisk.png")
divide1 = PhotoImage(file="icon/divide1.png")
clear = PhotoImage(file="icon/clear.png")
dot = PhotoImage(file="icon/dot.png")
tag = PhotoImage(file="icon/tag.png")
equal = PhotoImage(file="icon/equal.png")
power = PhotoImage(file="icon/power.png")
percent = PhotoImage(file="icon/percent.png")

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
btnD = Button(root, command=lambda:btnclick("."), font="popins 15 bold", width= 65, height=65, border=2, relief=SOLID, activebackground="black", bg="black", image=dot)
btnD.place(x=5, y=365)
btn0 = Button(root, font="popins 15 bold", width= 65, height=65, border=2, relief=SOLID, command=lambda:btnclick(0), activebackground="black", bg="black", image=zero)
btn0.place(x=80, y=365)
btnE = Button(root, font="popins 15 bold", width= 65, height=65, border=2, relief=SOLID, command=btnequalinput, activebackground="black", bg="black", image=equal)
btnE.place(x=155, y=365)
btnA = Button(root, font="popins 15 bold", width= 65, height=65, border=2, relief=SOLID, command=lambda:btnclick("+"), activebackground="black", bg="black", image=add)
btnA.place(x=230, y=365)
######################################################################################################################
btn1 = Button(root, font="popins 15 bold", width= 65, height=65, border=2, relief=SOLID, command=lambda:btnclick(1), activebackground="black", bg="black", image=one)
btn1.place(x=5, y=295)
btn2 = Button(root, font="popins 15 bold", width= 65, height=65, border=2, relief=SOLID, command=lambda:btnclick(2), activebackground="black", bg="black", image=two)
btn2.place(x=80, y=295)
btn3 = Button(root, font="popins 15 bold", width= 65, height=65, border=2, relief=SOLID, command=lambda:btnclick(3), activebackground="black", bg="black", image=three)
btn3.place(x=155, y=295)
btnS = Button(root, font="popins 15 bold", width= 65, height=65, border=2, relief=SOLID, command=lambda:btnclick("-"), activebackground="black", bg="black", image=minus)
btnS.place(x=230, y=295)
######################################################################################################################
btn4 = Button(root, font="popins 15 bold", width= 65, height=65, border=2, relief=SOLID, command=lambda:btnclick(4), activebackground="black", bg="black", image=four)
btn4.place(x=5, y=225)
btn5 = Button(root, font="popins 15 bold", width= 65, height=65, border=2, relief=SOLID, command=lambda:btnclick(5), activebackground="black", bg="black", image=five)
btn5.place(x=80, y=225)
btn6 = Button(root, font="popins 15 bold", width= 65, height=65, border=2, relief=SOLID, command=lambda:btnclick(6), activebackground="black", bg="black", image=six)
btn6.place(x=155, y=225)
btnM = Button(root, font="popins 15 bold", width= 65, height=65, border=2, relief=SOLID, command=lambda:btnclick("*"), activebackground="black", bg="black", image=asterisk)
btnM.place(x=230, y=225)
######################################################################################################################
btn7 = Button(root, font="popins 15 bold", width= 65, height=65, border=2, relief=SOLID, command=lambda:btnclick(7), activebackground="black", bg="black", image=seven)
btn7.place(x=5, y=155)
btn8 = Button(root, font="popins 15 bold", width= 65, height=65, border=2, relief=SOLID, command=lambda:btnclick(8), activebackground="black", bg="black", image=eight)
btn8.place(x=80, y=155)
btn9 = Button(root, font="popins 15 bold", width= 65, height=65, border=2, relief=SOLID, command=lambda:btnclick(9), activebackground="black", bg="black", image=nine)
btn9.place(x=155, y=155)
btnDIV = Button(root, font="popins 15 bold", width= 65, height=65, border=2, relief=SOLID, command=lambda:btnclick("/"), activebackground="black", bg="black", image=divide1)
btnDIV.place(x=230, y=155)
btnC = Button(root, font="popins 15 bold", width= 65, height=65, border=2, relief=SOLID, command=btncleardisplay, activebackground="black", bg="black", image=clear)
btnC.place(x=116, y=85)
######################################################################################################################

root.mainloop()