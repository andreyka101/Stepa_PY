from tkinter import *

window = Tk()
window.title('cashier')
window.geometry("600x500")
window.config(bg="#ffec19")



# создание элемента Canvas
canV = Canvas(height=500 , width=600 , bg="#fff")
canV.place(x=0 , y=0)

# сохраняем id фигуры в переменную
# r1 = canV.create_rectangle(120 ,150 , 500, 400 , fill="#38fac6" ,width=7 , outline="#127261")


# задаём тег фигуре
canV.create_rectangle(120 ,150 , 500, 400 , fill="#38fac6" ,width=7 , outline="#127261" , tags="i_rect")
canV.create_oval(200 ,300 , 600, 600 , fill="#8238FA" ,width=0  , tags="i_rect")




def fun(e):
    # coords - меняем координаты по id или тегу
    # itemconfig - меняем другие переменные по id или тегу

    # меняем фигуру по id
    # canV.coords(r1 , 0 , 0 , 200 , 200 )
    # canV.itemconfig(r1, fill="#FA3838" )


    # меняем фигуру по тегу 
    # canV.coords("i_rect" , 0 , 0 , 200 , 200 )
    canV.itemconfig("i_rect", fill="#FA3838")
window.bind("<MouseWheel>" , fun)
window.mainloop()