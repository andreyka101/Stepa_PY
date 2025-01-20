from tkinter import *

window = Tk()
window.title('cashier')
window.geometry("900x400")
window.config(bg="#ffec19")



text = Label(font=("" , 14))
text.place(x=30,y=150)



def motion(event):
    text.config(text=event)
    window.title('cashier')

window.bind("<Motion>" , motion)





window.mainloop()