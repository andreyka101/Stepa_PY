from tkinter import *


window = Tk()
window.title("lesson 11")
window.geometry("600x500")
window.config(bg="#e4ffa6")

# зафиксировать размер окна
window.resizable(False , False)

# минимальный размер окна
# window.minsize(400 , 300)

# максимальный размер окна
# window.maxsize(800 , 700)




# anchor позиционирование относительно окна
lab_text_1 = Label(text="325552", font=("MV Boli" , 15))
lab_text_1.place(relx= 0.5 , rely=0.5 , anchor="center")

lab_text_2 = Label(text="1111", font=("MV Boli" , 15))
lab_text_2.place(relx= 0.5 , rely=0.8 , anchor="center")





inp_ent = Entry()
inp_ent.place(x=30 , y=30)




def fun_del():
    global inp_ent
    print(inp_ent)
    # метод destroy() - удаляет элемент tkinter
    inp_ent.destroy()
    print(inp_ent)
but_1 = Button(text="del" , command=fun_del)
but_1.place(x=30 , y=90)




def fun():
    # меняем ширину высоту и координаты окна через Entry
    window.geometry(inp_ent.get())
but_1 = Button(text="run" , command=fun)
but_1.place(x=30 , y=120)



def fun_del_text():
    # очищаем Entry
    inp_ent.delete(0, END) 
but_1 = Button(text="del text" , command=fun_del_text)
but_1.place(x=30 , y=150)






window.mainloop()