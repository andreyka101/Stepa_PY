from tkinter import *

window = Tk()
window.title('cashier')
window.geometry("600x500")
window.config(bg="#ffec19")


canV = Canvas(height=500 , width=600 , bg="#fff")
canV.place(x=0 , y=0)


obj = {
    "x1" :None,
    "y1" :None,
    "x2" :None,
    "y2" :None,
}



def fun(event):
    global obj
    window.title(f"{event.x} {event.y}")
    # print(event.state)
    if(event.state == 264):
        # canV.create_oval(event.x-15 , event.y-15 ,event.x + 15 , event.y + 15 , fill="#ffb81f" , width=0)
        
        
        
        if(obj["x2"] == None):
            obj["x1"] = event.x
            obj["y1"] = event.y

        obj["x2"] = event.x
        obj["y2"] = event.y
        canV.create_line(obj["x1"] , obj["y1"], obj["x2"] , obj["y2"] , width=10)
        obj["x1"] = obj["x2"]
        obj["y1"] = obj["y2"]
    if(event.state == 8):
        obj = {
            "x1" :None,
            "y1" :None,
            "x2" :None,
            "y2" :None,
        }



    if(event.state == 1032):
        canV.create_oval(event.x-35 , event.y-35 ,event.x + 35 , event.y + 35 , fill="#ffffff" , width=0)

canV.bind("<Motion>" , fun)





window.mainloop()