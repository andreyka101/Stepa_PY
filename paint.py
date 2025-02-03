from tkinter import *

window = Tk()
window.title('cashier')
window.geometry("600x500")
window.config(bg="#ffec19")


canV = Canvas(height=500 , width=600 , bg="#fff")
canV.place(x=0 , y=0)




def fun(event):
    window.title(f"{event.x} {event.y}")
    # print(event.state)
    if(event.state == 264):
        canV.create_oval(event.x-15 , event.y-15 ,event.x + 15 , event.y + 15 , fill="#ffb81f" , width=0)

canV.bind("<Motion>" , fun)





window.mainloop()