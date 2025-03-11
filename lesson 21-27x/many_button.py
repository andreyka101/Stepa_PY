from tkinter import *

window = Tk()
window.title('cashier')
window.geometry("500x500")
window.config(bg="#ffee2f")



text = Label(font=("" , 14))
text.place(x=30,y=10)


obj_button = {}



num = 0
def fun(event):
    element = event.widget

    # text.config(text= element)

    # text.config(text= element["text"])

    global num
    num += int(element["text"].split(" ")[2])
    text.config(text= num)

    if(int(element["text"].split(" ")[2]) == 1):
        window.config(bg="#ffffff")
    elif(int(element["text"].split(" ")[2]) == 2):
        window.config(bg="#b8b8b8")
    elif(int(element["text"].split(" ")[2]) == 3):
        window.config(bg="#909090")
    elif(int(element["text"].split(" ")[2]) == 4):
        window.config(bg="#5b5b5b")
    elif(int(element["text"].split(" ")[2]) == 5):
        window.config(bg="#2a2a2a")



def motion(event):
    window.title(f"{event.x} {event.y}")



for i in range(1,6):
    obj_button[f"but{i}"] = Button(text=f'button num {i}')
    obj_button[f"but{i}"].place(x = 20 , y =40 * i)
    obj_button[f"but{i}"].bind("<Button-1>" , fun)
    obj_button[f"but{i}"].bind("<Motion>" , motion)




window.mainloop()