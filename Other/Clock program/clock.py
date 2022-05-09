from tkinter import *
from time import *

def update():
    week_string = strftime("%w:%A")
    week_label.config(text=week_string)

    time_string = strftime("%H:%M:%S")
    time_label.config(text=time_string)

    date_string = strftime("%B %d %Y")
    date_label.config(text=date_string)

    day_string = strftime("%x")
    day_label.config(text=day_string)

    window.after(1000,update)


window = Tk()



window.title("Clock")
window.geometry("500x400")
window.config(bg="black")
window.iconbitmap("clock.ico")

week_label = Label(window,font=("10468",50),fg="#cc0000",bg="Black")
week_label.pack()

time_label = Label(window,font=("10468",50),fg="#2a52be",bg="Black")
time_label.pack()

date_label = Label(window,font=("10468",50),fg="#FFD800",bg="Black")
date_label.pack()

day_label = Label(window,font=("10468",50),fg="#FF9900",bg="Black")
day_label.pack()

update()

window.mainloop()