from tkinter import *

window = Tk()
window.title('cashier')
window.geometry("900x400")
window.config(bg="#ffec19")



text = Label(font=("" , 14))
text.place(x=30,y=150)



def fun_press(event):
    # text.config(text=event)
    text.config(text=event.keysym)
    # text.config(text=event.keycode)
    # text.config(text=event.state)
    if(event.keycode == 87):
        window.config(bg="#238ecc")
    # if(event.keysym == "w"):
    #     window.config(bg="#238ecc")


    # if(event.keycode == 87 and event.state == 9):
    #     window.config(bg="#6b1385")
    if(event.keysym == "W" and event.state == 9):
        window.config(bg="#6b1385")

window.bind("<KeyPress>" , fun_press)




def fun_release(event):
    # text.config(text=event)
    # text.config(text=event.keysym)
    # text.config(text=event.keycode)
    # text.config(text=event.state)
    # if(event.keycode == 87):
    #     window.config(bg="#238ecc")
    if(event.keysym == "w"):
        window.config(bg="#cc2323")


    if(event.keycode == 87 and event.state == 9):
        window.config(bg="#3abc20")
    # if(event.keysym == "W" and event.state == 9):
    #     window.config(bg="#6b1385")

window.bind("<KeyRelease>" , fun_release)





window.mainloop()