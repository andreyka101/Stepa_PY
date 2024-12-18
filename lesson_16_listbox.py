from tkinter import *
from tkinter import ttk


window = Tk()
window.geometry("600x500")
window.config(bg="#e4ffa6")



# Listbox - Отображение списка в интерфейсе 
arr = [20,8,4,"qwe","rtrtrrt"]
list_box = Listbox(listvariable = Variable(value=arr))
list_box.place(x=30 , y=30 , height=100)




lab_text = Label(text="")
lab_text.place(x=30 , y=160)

inp_ent = ttk.Entry()
inp_ent.place(x=30 , y=190)




def fun_1():
    # list_box.curselection() - возвращает выбранный индекс 
    print(list_box.curselection())
    lab_text.config(text=list_box.curselection())
but_1 = Button(text='get index' , command=fun_1)
but_1.place(x=300 , y=50)




def fun_2():
    # list_box.get(i) - возвращает элемент индекса i
    print(list_box.get(0))
    lab_text.config(text=list_box.get(list_box.curselection()))
but_2 = Button(text='get element' , command=fun_2)
but_2.place(x=300 , y=80)




def fun_3():
    # list_box.insert(x , element) - вставляет новый элемент на x индекс
    list_box.insert(0, inp_ent.get())
but_3 = Button(text='insert 0' , command=fun_3)
but_3.place(x=300 , y=110)




def fun_4():
    # list_box.delete(i) - удаляет элемент по индексу i
    list_box.delete(list_box.curselection())
but_4 = Button(text='delete' , command=fun_4)
but_4.place(x=300 , y=140)




def fun_5():
    list_box.insert(list_box.curselection(), inp_ent.get())
    list_box.delete(list_box.curselection())
but_5 = Button(text='rename' , command=fun_5)
but_5.place(x=300 , y=170)




window.mainloop()