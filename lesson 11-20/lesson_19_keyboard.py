from tkinter import *

window = Tk()
window.title('cashier')
window.geometry("900x400")
window.config(bg="#ffec19")



text = Label(font=("" , 14))
text.place(x=30,y=150)



def fun_press(event):
    # event - получаем информацию о обработчике (клавиша)
    # text.config(text=event)

    # event.keysym - название клавиши
    text.config(text=event.keysym)

    # event.keycode - номер клавиши
    # text.config(text=event.keycode)

    # event.state - информация о дополнительно зажатых клавиш
    # text.config(text=event.state)

    if(event.keycode == 87):
        window.config(bg="#238ecc")
    # if(event.keysym == "w"):
    #     window.config(bg="#238ecc")

    # if(event.keycode == 87 and event.state == 9):
    #     window.config(bg="#6b1385")
    if(event.keysym == "W" and event.state == 9):
        window.config(bg="#6b1385")

# обработчик нажатия клавиши клавиатуры 
window.bind("<KeyPress>" , fun_press)




def fun_release(event):
    # event - получаем информацию о обработчике (клавиша)
    # text.config(text=event)

    # event.keysym - название клавиши
    # text.config(text=event.keysym)

    # event.keycode - номер клавиши
    # text.config(text=event.keycode)

    # event.state - информация о дополнительно зажатых клавиш
    text.config(text=event.state)

    # if(event.keycode == 87):
    #     window.config(bg="#238ecc")
    if(event.keysym == "w"):
        window.config(bg="#cc2323")


    if(event.keycode == 87 and event.state == 9):
        window.config(bg="#3abc20")
    # if(event.keysym == "W" and event.state == 9):
    #     window.config(bg="#6b1385")

# обработчик отжатия кл авиши клавиатуры
window.bind("<KeyRelease>" , fun_release)





window.mainloop()