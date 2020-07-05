from tkinter import *

def btnClick(numberes):
    global operator
    operator=operator + str(numberes)
    text_Inpt.set(operator)

def btnClear():
    global operator
    operator=""
    text_Inpt.set("")
    


calc = Tk()
calc.title("aDex_Calculator")
operator = ""
text_Inpt = StringVar()

textDisplay = Entry(calc, font=('aria', 20, 'bold'), textvariable=text_Inpt, bd=30, insertwidth=4, bg='#00B2BF',
              justify='right').grid(columnspan=4)

btnClear = Button(calc, padx=16, pady=3, bd=5, fg='black', bg='#CC0000', font=('aria', 20, 'bold'),
                  text='C', command=btnClear).grid(row=1, column=3)

btn7 = Button(calc, padx=16, bd=8, fg='#fff', bg='#002456', font=('aria', 20, 'bold'), text='7',
              command=lambda:btnClick(7)).grid(row=2, column=0)
btn8 = Button(calc, padx=16, bd=8, fg='#fff', bg='#002456', font=('aria', 20, 'bold'), text='8',
              command=lambda:btnClick(8)).grid(row=2, column=1)
btn9 = Button(calc, padx=16, bd=8, fg='#fff', bg='#002456', font=('aria', 20, 'bold'), text='9',
              command=lambda:btnClick(9)).grid(row=2, column=2)
btnAddition = Button(calc, padx=16, bd=8, fg='#fff', bg='#002456', font=('aria', 20, 'bold'), text='+',
              command=lambda:btnClick('+')).grid(row=2,column=3)


btn4 = Button(calc, padx=16, bd=8, fg='#fff', bg='#002456', font=('aria', 20, 'bold'), text='4',
              command=lambda:btnClick(4)).grid(row=3, column=0)
btn5 = Button(calc, padx=16, bd=8, fg='#fff', bg='#002456', font=('aria', 20, 'bold'), text='5',
              command=lambda:btnClick(5)).grid(row=3, column=1)
btn6 = Button(calc, padx=16, bd=8, fg='#fff', bg='#002456', font=('aria', 20, 'bold'), text='6',
              command=lambda:btnClick(6)).grid(row=3, column=2)
btnSubtraction = Button(calc, padx=20, bd=8, fg='#fff', bg='#002456', font=('aria', 20, 'bold'), text='-',
              command=lambda:btnClick('-')).grid(row=3, column=3)

btn1 = Button(calc, padx=16, bd=8, fg='#fff', bg='#002456', font=('aria', 20, 'bold'), text='1',
              command=lambda:btnClick(1)).grid(row=4, column=0)
btn2 = Button(calc, padx=16, bd=8, fg='#fff', bg='#002456', font=('aria', 20, 'bold'), text='2',
              command=lambda:btnClick(2)).grid(row=4, column=1)
btn3 = Button(calc, padx=16, bd=8, fg='#fff', bg='#002456', font=('aria', 20, 'bold'), text='3',
              command=lambda:btnClick(3)).grid(row=4, column=2)
btnMultiplication = Button(calc, padx=16, bd=8, fg='#fff', bg='#002456', font=('aria', 20, 'bold'), text='X',
              command=lambda:btnClick('X')).grid(row=4, column=3)

btnDot = Button(calc, padx=16, bd=8, fg='#fff', bg='#002456', font=('aria', 20, 'bold'), text='.',
              command=lambda:btnClick('.')).grid(row=5, column=0)
btn0 = Button(calc, padx=16, bd=8, fg='#fff', bg='#002456', font=('aria', 20, 'bold'), text='0',
              command=lambda:btnClick(0)).grid(row=5, column=1)
btnEqual = Button(calc, padx=16, bd=8, fg='#fff', bg='#002456', font=('aria', 20, 'bold'), text='=').grid(row=5, column=2)
btnDivisio4 = Button(calc, padx=20, bd=8, fg='#fff', bg='#002456', font=('aria', 20, 'bold'), text='/',
              command=lambda:btnClick('/')).grid(row=5,column=3)

calc.mainloop()
