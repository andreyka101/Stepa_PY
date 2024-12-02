from tkinter import *


window = Tk()
window.title("lesson 11")
window.geometry("600x500")


lab_text_1 = Label(text="325552" , bg="#1ec5ef")
lab_text_1.place(x=300 , y=200 , width=100 , height=100)

lab_text_2 = Label(text="hello12345" , bg="#2d3d41" , fg= "#d3ff0c" , font=("MV Boli" , 15))
lab_text_2.place(x=30 , y=20)


def fun_1():
    print("ok")
    lab_text_1.place(x=100 , y=100)
    # lab_text_2.configure(text="nxxx540")
    lab_text_2.config(text="nxxx540",fg= "#ffb300")

button_1 = Button(text="start" , command=fun_1)
button_1.place(x=30 , y=60)



def fun_2():
    print(window.geometry())
    lab_text_2.config(text=window.geometry())

button_2 = Button(text="get_geometry" , command=fun_2)
button_2.place(x=30 , y=100)










window.mainloop()