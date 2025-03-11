from tkinter import *
from tkinter import ttk

window = Tk()
window.title('cashier')
window.geometry("400x400")
window.config(bg="#ffec19")



scale_1 = Scale(orient=HORIZONTAL)
scale_1.place(x=30,y=30)



def fun(event):
    # print(type(event))
    # text.config(text= event)
    # text.config(text= round(float(event) , 0))
    text.config(text= int(float(event)))
    # text.place(x=int(float(event)))

scale_2 = ttk.Scale(command=fun , from_= 1 , to=5 , length=200)
scale_2.place(x=30,y=100)


# scale_3 = ttk.Scale(orient=VERTICAL)
# scale_3.place(x=200,y=30)



def fun_2():
    text.config(text=scale_2.get())
but = Button(text="but" , command=fun_2)
but.place(x=150 , y=30)


text = Label(font=("" , 14))
text.place(x=30,y=150)


window.mainloop()