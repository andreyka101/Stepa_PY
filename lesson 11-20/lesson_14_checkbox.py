from tkinter import *


window = Tk()
window.title("lesson 11")
window.geometry("600x500")
window.config(bg="#e4ffa6")




def fun():
    # получаем положение Checkbutton
    lab_text.config(text=num_check.get())
    if(num_check.get()):
        window.config(bg="#ff4949")
    else:
        window.config(bg="#49c8ff")


# в num_check хранится положения Checkbutton
num_check = IntVar(value=1)
# Checkbutton это кнопка с двумя положениями
checkbox = Checkbutton(text="eigfuegf" , variable=num_check , command=fun)
checkbox.place(x=30 , y=30)

lab_text = Label()
lab_text.place(x=30 , y=60)
# fun()


window.mainloop()