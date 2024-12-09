from tkinter import *


window = Tk()
window.title("lesson 11")
window.geometry("600x500")
window.config(bg="#e4ffa6")



def fun():
    lab_text.config(text= inp_ent.get())

inp_ent = Entry()
inp_ent.place(x=30 , y=30)
lab_text = Label()
lab_text.place(x=30 , y=60)


but_1 = Button(text="run" , command=fun)
but_1.place(x=30 , y=90)


window.mainloop()