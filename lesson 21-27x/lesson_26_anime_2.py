from tkinter import *
import time


# https://easings.net/ru


window = Tk()
window.title('cashier')
window.geometry("600x500")
window.config(bg="#ffec19")



canV = Canvas(height=500 , width=600 , bg="#fff")
canV.place(x=0 , y=0)




# photo = PhotoImage(file="all_photo/Sprite-0002.png")
# canV.create_image(300 , 250, image=photo )



# анимация фото
time_save = int(round(time.time() , 2) * 100)
while(int(round(time.time() , 2) * 100)+ 160 != int(round(time.time() , 2) * 100)):

    time_now = int(round(time.time() , 2) * 100)
    print(time_save, int(round(time.time() , 2) * 100))

    canV.update()

    print(time_save - time_now)
    photo = PhotoImage(file=f"all_photo/Sprite-000{((time_now - time_save)//20)+2}.png")
    canV.create_image(300 , 250, image=photo )



window.mainloop()