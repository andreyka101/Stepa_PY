from tkinter import *
from random import randrange

window = Tk()
window.title('cashier')
window.geometry("600x500")
window.config(bg="#ffec19")


canV = Canvas(height=500 , width=600 , bg="#fff")
canV.place(x=0 , y=0)


robot_obj = {
    "x1" :0,
    "y1" :0,
    "x2" :50,
    "y2" :50,
}


rand_x = randrange(0 , 11)
rand_y = randrange(0 , 9)
coin_obj = {
    "x1" : 50 * rand_x,
    "y1" :50 * rand_y,
    "x2" : (50 * rand_x) + 50,
    "y2" :(50 * rand_y) + 50,
}

canV.create_rectangle(robot_obj["x1"] , robot_obj["y1"], robot_obj["x2"] , robot_obj["y2"] , fill="#ff382e" , width=0)
canV.create_oval(robot_obj["x1"] , robot_obj["y1"], robot_obj["x2"] , robot_obj["y2"] , fill="#2ed9ff" , width=0)

def fun(event):
    print(event.keycode)
    if(event.keycode == 83 and robot_obj["y2"] < 500):
        robot_obj["y1"] += 50
        robot_obj["y2"] += 50
    if(event.keycode == 68 and robot_obj["x2"] < 600):
        robot_obj["x1"] += 50
        robot_obj["x2"] += 50
    if(event.keycode == 87 and robot_obj["y1"] > 0):
        robot_obj["y1"] -= 50
        robot_obj["y2"] -= 50
    if(event.keycode == 65 and robot_obj["x1"] > 0):
        robot_obj["x1"] -= 50
        robot_obj["x2"] -= 50


    canV.create_rectangle(0,0, 600 , 500, fill="#ffffff" , width=0)
    canV.create_rectangle(robot_obj["x1"] , robot_obj["y1"], robot_obj["x2"] , robot_obj["y2"] , fill="#2e5bff" , width=0)



window.bind("<KeyPress>" , fun)

window.mainloop()