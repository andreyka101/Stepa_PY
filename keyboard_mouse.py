from tkinter import *
import pyautogui

window = Tk()
window.title('cashier')
window.geometry("900x400")
window.config(bg="#ffec19")



text = Label(font=("" , 14))
text.place(x=30,y=150)



def fun_press(event):
    text.config(text=event)
    # pyautogui.moveTo(event.x, event.y + 29)
    if(event.keycode == 38):
        window.config(bg="#238ecc")
        pyautogui.moveTo(event.x, event.y + 9)
    if(event.keycode == 40):
        window.config(bg="#238ecc")
        pyautogui.moveTo(event.x, event.y + 49)


window.bind("<KeyPress>" , fun_press)






window.mainloop()