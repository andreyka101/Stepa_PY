# импортируем библиотеку tkinter
from tkinter import *


# создаём окно 
window = Tk()
# меняем название окна
window.title("lesson 11")
# меняем ширину и высоту окна 
window.geometry("600x500")




# создаём текст через Label
# bg= цвет фона 
# fg= цвет текстам
# font = шрифт и размер текста 
lab_text_1 = Label(text="325552" , bg="#1ec5ef")
# placе - позиция и размер элемента
lab_text_1.place(x=300 , y=200 , width=100 , height=100)


lab_text_2 = Label(text="hello12345" , bg="#2d3d41" , fg= "#d3ff0c" , font=("MV Boli" , 15))
lab_text_2.place(x=30 , y=20)


def fun_1():
    print("ok")
    # изменяем позицию lab_text_1
    lab_text_1.place(x=100 , y=100)

    # с помощью метода configure или config можно изменить параметры объекта 
    # lab_text_2.configure(text="nxxx540")
    lab_text_2.config(text="nxxx540",fg= "#ffb300")

# создаём кнопку command вызывает функцию
button_1 = Button(text="start" , command=fun_1)
button_1.place(x=30 , y=60)



def fun_2():
    # window.geometry() выводит ширину высоту и координаты окна 
    print(window.geometry())
    lab_text_2.config(text=window.geometry())

button_2 = Button(text="get_geometry" , command=fun_2)
button_2.place(x=30 , y=100)










window.mainloop()