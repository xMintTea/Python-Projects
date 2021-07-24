from tkinter import *
from tkinter import messagebox

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text

    try:
        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except ZeroDivisionError:
        messagebox.showerror(title="Ошибка", message="Ты не можешь делить на ноль, идиот")

    except SyntaxError:
        messagebox.showerror(title="Ошибка", message="Ты можешь делать действия только с числами")

def clear():
    global equation_text

    equation_label.set("")

    equation_text = ("")


window = Tk()
window.title("Calculator program")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("consolas",20),bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, width=10,height=5,font=35,
                command = lambda: button_press(1))
button1.grid(row=0,column=0)

button2 = Button(frame, text=2, width=10,height=5,font=35,
                command = lambda: button_press(2))

button2.grid(row=0,column=1)

button3 = Button(frame, text=3, width=10,height=5,font=35,
                command = lambda: button_press(3))

button3.grid(row=0,column=2)

button4 = Button(frame, text=4, width=10,height=5,font=35,
                command = lambda: button_press(4))
button4.grid(row=1,column=0)

button5 = Button(frame, text=5, width=10,height=5,font=35,
                command = lambda: button_press(5))

button5.grid(row=1,column=1)

button6 = Button(frame, text=6, width=10,height=5,font=35,
                command = lambda: button_press(6))

button6.grid(row=1,column=2)

button7 = Button(frame, text=7, width=10,height=5,font=35,
                command = lambda: button_press(7))
button7.grid(row=2,column=0)

button8 = Button(frame, text=8, width=10,height=5,font=35,
                command = lambda: button_press(8))

button8.grid(row=2,column=1)

button9 = Button(frame, text=9, width=10,height=5,font=35,
                command = lambda: button_press(9))

button9.grid(row=2,column=2)

button0 = Button(frame, text=0, width=10,height=5,font=35,
                command = lambda: button_press(0))

button0.grid(row=3,column=0)

plus = Button(frame, text="+", width=10,height=5,font=35,
                command = lambda: button_press('+'))

plus.grid(row=0,column=3)

minus = Button(frame, text="-", width=10,height=5,font=35,
                command = lambda: button_press('-'))

minus.grid(row=1,column=3)

mult = Button(frame, text="*", width=10,height=5,font=35,
                command = lambda: button_press('*'))

mult.grid(row=2,column=3)

dev = Button(frame, text="/", width=10,height=5,font=35,
                command = lambda: button_press('/'))

dev.grid(row=3,column=3)

equal = Button(frame, text="=", width=10,height=5,font=35,
                command = equals)

equal.grid(row=3,column=2)

dote = Button(frame, text=".", width=10,height=5,font=35,
                command = lambda: button_press('.'))

dote.grid(row=3,column=1)

clear = Button(window, text="Clear", width=43,height=5,font=35,
                command = clear)

clear.pack()


window.mainloop()