from tkinter import *


window = Tk()
window.title("lesson 11")
window.geometry("600x500")
window.config(bg="#e4ffa6")
window.resizable(False , False)
# window.minsize(400 , 300)
# window.maxsize(800 , 700)


lab_text_1 = Label(text="325552", font=("MV Boli" , 15))
lab_text_1.place(relx= 0.5 , rely=0.5 , anchor="center")

lab_text_2 = Label(text="1111", font=("MV Boli" , 15))
lab_text_2.place(relx= 0.5 , rely=0.8 , anchor="center")





def fun_del():
    # window.geometry(inp_ent.get())
    global inp_ent
    print(inp_ent)
    inp_ent.destroy()
    print(inp_ent)



but_1 = Button(text="del" , command=fun_del)
but_1.place(x=30 , y=90)



inp_ent = Entry()
inp_ent.place(x=30 , y=30)

def fun():
    window.geometry(inp_ent.get())
but_1 = Button(text="run" , command=fun)
but_1.place(x=30 , y=120)



def fun_del_text():
    inp_ent.delete(0, END) 
but_1 = Button(text="del text" , command=fun_del_text)
but_1.place(x=30 , y=150)






window.mainloop()