from tkinter import *

window = Tk()
window.title('cashier')
window.geometry("600x500")
window.config(bg="#ffec19")



# создание элемента Canvas
canV = Canvas(height=500 , width=600 , bg="#fff")
canV.place(x=0 , y=0)
# рисуем в Canvas с помощью методов



# create_line - создать линию
# fill = цвет
# width = толщина линии
# smooth = закругление углов
canV.create_line(20 ,50 , 400, 300 , 400 , 30 , 10 , 300 , fill= "#ff2626" , width=6 , smooth=True)



# create_rectangle - создать квадрат
# fill = цвет
# width = толщина рамки
# outline = цвет рамки
canV.create_rectangle(120 ,150 , 500, 400 , fill="#38fac6" ,width=7 , outline="#127261")



# очистка Canvas
canV.create_rectangle(0 ,0 , 600, 500 , fill="#ffffff" ,width=0)



# create_oval - создать овал или круг
# fill = цвет
# width = толщина рамки
# outline = цвет рамки
# canV.create_oval(100 ,100 , 400, 400 , fill="#4538fa" ,width=7 , outline="#1b1a5c")



# create_polygon - создать многоугольник
# fill = цвет
# width = толщина рамки
# outline = цвет рамки
# canV.create_polygon(20 ,50 , 400, 300 ,400 , 30 , 10 , 300   , fill="#ffff2f" , width=6  , outline="#750606")





# create_arc - создаёт дугу

# start = начальный угол дуги в градусах;
# extent = размер дуги в градусах. Дуга всегда рисуется в направлении 
# против часовой стрелки;
# fill = цвет
# width = толщина линии дуги
# outline = цвет рамки
# canV.create_arc(100 ,100 , 400, 400 , fill="#1dff4e" , start = 0 , extent = 200)


# style ='arc' - рамка дуги
canV.create_arc(100 ,100 , 400, 400 , fill="#1dff4e" , start = 0 , extent = 200 , style = "arc" , outline="#f8d143" , width=80)


# style ='pieslice' - дуга с углом (стоит по умолчанию)
# canV.create_arc(100 ,100 , 400, 400 , fill="#1dff4e" , start = 0 , extent = 100 , style = "pieslice")


# style ='chord' - дуга без угла
canV.create_arc(100 ,100 , 400, 400 , fill="#1dff4e" , start = 0 , extent = 100 , style = "chord")



canV.create_text(200 , 300 , text="wertyui\nowguwuegefe\nefefeff\,efee\nefefefef" , justify = "center" , font="Georgia 15" , fill="#21B297")






window.mainloop()