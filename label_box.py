from tkinter import *

window = Tk()
window.title('cashier')
window.geometry("500x500")
window.config(bg="#fffbce")



lab_1 = Label(bg="#ff2424")
lab_1.place(x=0 , y=0 , width=250 ,height=250)

lab_2 = Label(bg="#fff82b")
lab_2.place(x=250 , y=0 , width=250 ,height=250)

lab_3 = Label(bg="#26FF22")
lab_3.place(x=0 , y=250 , width=250 ,height=250)

lab_4 = Label(bg="#22FFF8")
lab_4.place(x=250 , y=250 , width=250 ,height=250)
# print(lab_4)


text = Label(font=("" , 14))
text.place(x=30,y=150)



def motion(event):
    window.title(f"{event.x} {event.y}")

    # print(event.widget)

    # element = event.widget
    # element.config(bg="#9020ff")

window.bind("<Motion>" , motion)





def fun_b1(event):
    
    element = event.widget
    # print(type(element))
    text.config(text=element)
    # element
    if(str(element) == ".!label" or str(element) == ".!label2" or str(element) == ".!label3" or str(element) == ".!label4"):
        element.config(bg="#424242")

window.bind("<Button-1>" , fun_b1)



def fun_b3(event):
    
    element = event.widget
    # print(type(element))
    text.config(text=element)
    # element
    if(str(element) == ".!label" or str(element) == ".!label2" or str(element) == ".!label3" or str(element) == ".!label4"):
        element.config(bg="#dedede")

window.bind("<Button-3>" , fun_b3)




window.mainloop()

#! LabelFrame