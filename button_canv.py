from tkinter import *
from random import randrange

window = Tk()
window.title('0')
window.geometry("600x500")
window.config(bg="#FFF")


canV = Canvas(height=500 , width=600 , bg="#FFFFFF")
canV.place(x=0 , y=0)


button_arr = [
    {
        "x1":30,
        "y1":60,
        "x2":200,
        "y2":150,
        "background":"#F7FF18",
        "click": False,
        "text": "but 1"
    },
    {
        "x1":300,
        "y1":100,
        "x2":500,
        "y2":200,
        "background":"#43B7FF",
        "click": False,
        "text": "Hello World"
    },
]
for obj_i in button_arr:
    canV.create_rectangle(obj_i["x1"],obj_i["y1"] , obj_i["x2"],obj_i["y2"] , fill=obj_i["background"] , width=0)
    canV.create_text((obj_i["x1"] + obj_i["x2"])/2 , (obj_i["y1"] + obj_i["y2"])/2 , text=obj_i["text"] , justify = "center" , font="Georgia 15" , fill="#000000")




def motion(event):
    window.title(f"{event.x} {event.y}")
    
    for obj_i in button_arr:
        if(obj_i["click"]):
            canV.create_rectangle(obj_i["x1"],obj_i["y1"] , obj_i["x2"],obj_i["y2"] , fill="#FF0B0B", width=0)
            canV.create_text((obj_i["x1"] + obj_i["x2"])/2 , (obj_i["y1"] + obj_i["y2"])/2 , text=obj_i["text"] , justify = "center" , font="Georgia 15" , fill="#000000")
        elif((event.x > obj_i["x1"] and event.x < obj_i["x2"]) and (event.y > obj_i["y1"] and event.y < obj_i["y2"])):
            canV.create_rectangle(obj_i["x1"],obj_i["y1"] , obj_i["x2"],obj_i["y2"] , fill="#5D5D5D", width=0)
            canV.create_text((obj_i["x1"] + obj_i["x2"])/2 , (obj_i["y1"] + obj_i["y2"])/2 , text=obj_i["text"] , justify = "center" , font="Georgia 15" , fill="#000000")
        else:
            canV.create_rectangle(obj_i["x1"],obj_i["y1"] , obj_i["x2"],obj_i["y2"] , fill=obj_i["background"], width=0)
            canV.create_text((obj_i["x1"] + obj_i["x2"])/2 , (obj_i["y1"] + obj_i["y2"])/2 , text=obj_i["text"] , justify = "center" , font="Georgia 15" , fill="#000000")

window.bind("<Motion>" , motion)




def fun_b1(event):
    for obj_i in button_arr:
        if((event.x > obj_i["x1"] and event.x < obj_i["x2"]) and (event.y > obj_i["y1"] and event.y < obj_i["y2"])):
            canV.create_rectangle(obj_i["x1"],obj_i["y1"] , obj_i["x2"],obj_i["y2"] , fill="#FF0B0B", width=0)
            canV.create_text((obj_i["x1"] + obj_i["x2"])/2 , (obj_i["y1"] + obj_i["y2"])/2 , text=obj_i["text"] , justify = "center" , font="Georgia 15" , fill="#000000")
            obj_i["click"] = True
        # if((event.x < obj_i["x1"] or event.x > obj_i["x2"])):
        #     print("ok")
        if((event.x < obj_i["x1"] or event.x > obj_i["x2"]) or (event.y < obj_i["y1"] or event.y > obj_i["y2"])):
            canV.create_rectangle(obj_i["x1"],obj_i["y1"] , obj_i["x2"],obj_i["y2"] , fill=obj_i["background"], width=0)
            canV.create_text((obj_i["x1"] + obj_i["x2"])/2 , (obj_i["y1"] + obj_i["y2"])/2 , text=obj_i["text"] , justify = "center" , font="Georgia 15" , fill="#000000")
            obj_i["click"] = False
        
            

window.bind("<Button-1>" , fun_b1)


window.mainloop()