from tkinter import *

gui=Tk()
gui.title("calculater")
gui.geometry("410x360+700+50")
gui.resizable(0,0)

def press(no):
    equation.set(" ")
    global expression
    expression = expression + str(no)  
    equation.set(expression)
    
def equal():
    try:    
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=total
    except:
        
        expression=" "
        equation.set("")
        
def clear():
    global expression
    expression="" 
    equation.set("")

expression=""
equation=StringVar()
equation.set(" ")

expression_field = Entry(gui, textvariable=equation,bd=5,justify=RIGHT,font=("Times New Roman",30)) 
expression_field.grid(columnspan=4)
 
button1 = Button(gui, text='1',command=lambda:press(1), height=2, width=10) 
button1.grid(row=2, column=0,padx=10,pady=10)
    
button2 = Button(gui, text='2',command=lambda: press(2), height=2, width=10) 
button2.grid(row=2, column=1)
    
button3 = Button(gui, text='3',command=lambda: press(3), height=2, width=10) 
button3.grid(row=2, column=2)

button4 = Button(gui, text='4',command=lambda: press(4), height=2, width=10) 
button4.grid(row=3, column=0)

button5 = Button(gui, text='5',command=lambda: press(5), height=2, width=10) 
button5.grid(row=3, column=1)

button6 = Button(gui, text='6',command=lambda: press(6), height=2, width=10) 
button6.grid(row=3, column=2)

button7 = Button(gui, text='7',command=lambda: press(7), height=2, width=10) 
button7.grid(row=4, column=0)

button8 = Button(gui, text='8',command=lambda: press(8), height=2, width=10) 
button8.grid(row=4, column=1)

button9 = Button(gui, text='9',command=lambda: press(9), height=2, width=10) 
button9.grid(row=4, column=2,padx=10,pady=10)

button0 = Button(gui, text='0',command=lambda: press(0), height=2, width=10) 
button0.grid(row=5, column=1)

buttonplus = Button(gui, text='+',command=lambda: press("+"), height=2, width=10) 
buttonplus.grid(row=2, column=3)

buttonmin = Button(gui, text='-',command=lambda: press("-"), height=2, width=10) 
buttonmin.grid(row=3, column=3)

buttonmul = Button(gui, text='*',command=lambda: press("*"), height=2, width=10) 
buttonmul.grid(row=4, column=3)

buttondiv = Button(gui, text='/',command=lambda: press("/"), height=2, width=10) 
buttondiv.grid(row=5, column=3)

buttoneql = Button(gui, text='=',command=equal, height=2, width=10) 
buttoneql.grid(row=5, column=2)

buttonclr = Button(gui, text='clear',command=clear, height=2, width=10) 
buttonclr.grid(row=5, column=0)

labletxt=Label(gui,text="calculater",height=2,width=10,font=("Elephant",30,"bold"))
labletxt.grid(columnspan=4,sticky=S)
gui.mainloop()