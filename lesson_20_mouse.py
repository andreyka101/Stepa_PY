from tkinter import *

window = Tk()
window.title('cashier')
window.geometry("900x400")
window.config(bg="#ffec19")



text = Label(font=("" , 14))
text.place(x=30,y=150)



def motion(event):
    # text.config(text=event)
    window.title(f"{event.x} {event.y}")

    # text.config(text=event.state)

window.bind("<Motion>" , motion)



# def fun_b1(event):
#     text.config(text=event)

# window.bind("<Button-1>" , fun_b1)



# def fun_b2(event):
#     text.config(text=event)

# window.bind("<Button-2>" , fun_b2)



# def fun_b3(event):
#     text.config(text=event)

# window.bind("<Button-3>" , fun_b3)



num_wheel = 30
def fun_mouseWheel(event):
    global num_wheel
    text.config(text=event)
    if(event.delta == 120):
        num_wheel += 10
    else:
        num_wheel-= 10
    text.place(y=num_wheel)

window.bind("<MouseWheel>" , fun_mouseWheel)





window.mainloop()