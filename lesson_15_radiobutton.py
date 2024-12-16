from tkinter import *
from tkinter import ttk


window = Tk()
window.geometry("600x500")
window.config(bg="#e4ffa6")



def fun_1():
    lab_text.config(text=num_radio.get())
    if(num_radio.get() == "n1"):
        window.config(bg="#ff0000")
    if(num_radio.get() == "n2"):
        window.config(bg="#930000")
    if(num_radio.get() == "n3"):
        window.config(bg="#480000")



num_radio = StringVar()

radio_1 = ttk.Radiobutton(text="b1" , variable=num_radio , value="n1" , command=fun_1)
radio_1.place(x=30 , y =30)
radio_2 = ttk.Radiobutton(text="b2", variable=num_radio , value="n2" , command=fun_1)
radio_2.place(x=30 , y =60)
radio_3 = ttk.Radiobutton(text="b3", variable=num_radio , value="n3" , command=fun_1)
radio_3.place(x=30 , y =90)



lab_text = Label(text=num_radio.get())
lab_text.place(x=30 , y =150)




window.mainloop()