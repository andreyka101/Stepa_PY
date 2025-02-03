from tkinter import *

window = Tk()
window.title('cashier')
window.geometry("600x500")
window.config(bg="#ffec19")


canV = Canvas(height=500 , width=600 , bg="#fff")
canV.place(x=0 , y=0)



canV.create_line(20 ,50 , 400, 300 , 400 , 30 , 10 , 300 , fill= "#ff2626" , width=6 , smooth=True)




canV.create_rectangle(120 ,150 , 500, 400 , fill="#38fac6" ,width=7 , outline="#127261")



canV.create_rectangle(0 ,0 , 600, 500 , fill="#ffffff" ,width=0)



# canV.create_oval(100 ,100 , 400, 400 , fill="#4538fa" ,width=7 , outline="#1b1a5c")



# canV.create_polygon(20 ,50 , 400, 300 ,400 , 30 , 10 , 300   , fill="#ffff2f" , width=6  , outline="#750606")



# canV.create_arc(100 ,100 , 400, 400 , fill="#1dff4e" , start = 0 , extent = 200)



canV.create_arc(100 ,100 , 400, 400 , fill="#1dff4e" , start = 0 , extent = 200 , style = "arc" , outline="#f8d143" , width=80)



# canV.create_arc(100 ,100 , 400, 400 , fill="#1dff4e" , start = 0 , extent = 100 , style = "pieslice")



canV.create_arc(100 ,100 , 400, 400 , fill="#1dff4e" , start = 0 , extent = 100 , style = "chord")



















window.mainloop()