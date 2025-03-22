from tkinter import *
import time


# https://easings.net/ru


window = Tk()
window.title('cashier')
window.geometry("600x500")
window.config(bg="#ffec19")



canV = Canvas(height=500 , width=600 , bg="#fff")
canV.place(x=0 , y=0)



obj={
    "x1":0,
    "x2":50,
    "y1":10,
    "y2":60,
}
canV.create_rectangle(obj["x1"],obj["y1"] , obj["x2"],obj["y2"] , fill="#762CFF", width=0)


# анимация простая
# time_save = int(time.time())
# while(time_save + 20 != int(time.time())):
    # print(time_save + 200 , "–" , time.time())
    # print(int(time.time()) - time_save)

    # canV.update()

#     canV.create_rectangle(obj["x1"] + (int(time.time()) - time_save),obj["y1"] , obj["x2"] + (int(time.time()) - time_save),obj["y2"] , fill="#762CFF", width=0)


# вид анимации
    # time_now = int(time.time())
    # canV.create_rectangle(0,0 , 600,500 , width=0 ,fill="#ffffff")
    # canV.create_rectangle(obj["x1"] + (time_now - time_save)*(time_now - time_save),obj["y1"] , obj["x2"] + (time_now - time_save)*(time_now - time_save),obj["y2"] , fill="#762CFF", width=0)




# анимация с разной скоростью
# time_save = int(round(time.time() , 2) * 100)
# while(time_save + 2 != int(round(time.time() , 2) * 100)):
#     time_now = int(round(time.time() , 2) * 100)
#     print(time.time(), int(round(time.time() , 2) * 100))

#     canV.update()

#     canV.create_rectangle(0,0 , 600,500 , width=0 ,fill="#ffffff")
#     canV.create_rectangle(obj["x1"] + (time_now - time_save)*(time_now - time_save),obj["y1"] , obj["x2"] + (time_now - time_save)*(time_now - time_save),obj["y2"] , fill="#762CFF", width=0)



window.mainloop()


